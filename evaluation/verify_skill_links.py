"""Check repository structure and local links; this does not evaluate agent behavior."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "design-quality", "design-ui", "domain-modeling", "explain-work", "grilling",
    "implement", "implement-spec", "setup-project-skills", "task-loop", "to-spec", "to-tickets",
}
MANUAL = {"design-ui", "setup-project-skills", "task-loop", "to-spec", "to-tickets"}


def headings(source):
    slugs, seen = set(), {}
    for title in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", source, re.M):
        title = re.sub(r"<[^>]+>", "", title).lower().replace("`", "")
        slug = re.sub(r"[^\w\- ]", "", title).replace(" ", "-")
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        slugs.add(f"{slug}-{count}" if count else slug)
    return slugs


def run():
    skills = ROOT / "skills"
    found = {p.name for p in skills.iterdir() if p.is_dir()}
    assert found == EXPECTED, f"Unexpected skill set: {found ^ EXPECTED}"
    for name in sorted(EXPECTED):
        path = skills / name / "SKILL.md"
        source = path.read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---(?:\n|$)", source, re.S)
        assert match, f"{name}: invalid frontmatter"
        meta = match.group(1)
        assert re.search(fr"^name: {re.escape(name)}$", meta, re.M), f"{name}: incorrect name"
        assert re.search(r"^description: \S.+", meta, re.M), f"{name}: missing description"
        disabled = re.findall(r"^disable-model-invocation:\s*(\S+)\s*$", meta, re.M)
        assert disabled == (["true"] if name in MANUAL else []), f"{name}: incorrect manual trigger"
        ui = skills / name / "agents" / "openai.yaml"
        assert ui.exists(), f"{name}: missing UI metadata"
        metadata = ui.read_text(encoding="utf-8")
        for field in ("display_name", "short_description", "default_prompt"):
            assert re.search(fr'^  {field}: ".+"$', metadata, re.M), f"{name}: missing {field}"
        assert f"${name}" in metadata, f"{name}: default prompt omits skill name"
        policy = re.findall(r"^  allow_implicit_invocation:\s*(\S+)\s*$", metadata, re.M)
        if name in MANUAL:
            assert policy == ["false"], f"{name}: implicit invocation must be disabled"
            assert re.search(r"^policy:\s*$", metadata, re.M), f"{name}: missing policy section"
        else:
            assert policy in ([], ["true"]), f"{name}: unexpected manual-only policy"
        assert not re.search(r"^user-invocable:\s*false\s*$", meta, re.M), f"{name}: user entry is hidden"

    count = 0
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        source = path.read_text(encoding="utf-8")
        # Code examples may contain placeholder links; only check prose links.
        source = re.sub(r"^```.*?^```[^\n]*$", "", source, flags=re.M | re.S)
        for raw in re.findall(r"\]\(([^)]+)\)", source):
            raw = raw.strip().split(' "', 1)[0].strip("<>")
            url = urlsplit(raw)
            if url.scheme or url.netloc:
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            assert target.is_relative_to(ROOT), f"{path.relative_to(ROOT)}: link escapes repository: {raw}"
            assert target.exists(), f"{path.relative_to(ROOT)}: missing link target: {raw}"
            if url.fragment and target.suffix == ".md":
                assert unquote(url.fragment) in headings(target.read_text(encoding="utf-8")), f"{path.relative_to(ROOT)}: missing heading: {raw}"
            count += 1
    print(f"PASS: {len(EXPECTED)} skills, {len(MANUAL)} manual entries, metadata, and {count} local links; no behavior claim")


if __name__ == "__main__":
    try:
        run()
    except (AssertionError, OSError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
