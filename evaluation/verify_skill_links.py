"""Static regression checks; no LLM calls and no claims about model behavior."""
from pathlib import Path
import re, sys

ROOT=Path(__file__).resolve().parents[1]
SKILLS=ROOT/'skills'
EXPECTED={'design-ui','domain-modeling','explain-work','grilling','implement-spec','implement','setup-project-skills','to-spec','to-tickets'}

def run():
    found={p.name for p in SKILLS.iterdir() if p.is_dir()}
    assert found==EXPECTED, f'Unexpected skill set: {found ^ EXPECTED}'
    for name in EXPECTED:
        path=SKILLS/name/'SKILL.md'
        source=path.read_text(encoding='utf-8')
        assert source.startswith('---\n'), f'{name}: no frontmatter'
        meta=source.split('---\n',2)[1]
        assert re.search(fr'^name: {re.escape(name)}$',meta,re.M),f'{name}: incorrect name'
        assert re.search(r'^description: .+',meta,re.M),f'{name}: missing description'
        assert '代码' in source and '已确认' in source,f'{name}: missing fact/goal priority'
        for rel in re.findall(r'\]\(([^)]+\.md)\)',source):
            if rel.startswith(('https://','http://')): continue
            assert (path.parent/rel).exists(),f'{name}: broken link {rel}'
    grill=(SKILLS/'grilling'/'SKILL.md').read_text('utf-8')
    assert all(x in grill for x in ('两个或更多','不附建议','已选含义'))
    spec=(SKILLS/'to-spec'/'SKILL.md').read_text('utf-8')
    assert '缩小' in spec and '多份 Spec' in spec and 'spec-template.md' in spec
    issue=(SKILLS/'to-tickets'/'SKILL.md').read_text('utf-8')
    assert all(x in issue for x in ('issue-template.md','依赖','失败场景'))
    design=(SKILLS/'design-ui'/'SKILL.md').read_text('utf-8')
    assert design.index('## 先做 design-board.html') < design.index('## 再从采用的设计提取 Token')
    assert 'design-quality.md' in design and '真实接口状态' in design
    multi=(SKILLS/'implement-spec'/'SKILL.md').read_text('utf-8')
    assert '收敛' in multi and '已授权' in multi and '跨规格' in multi
    assert (ROOT/'EVALUATION.md').exists()
    print('PASS: 9 skills, frontmatter, internal links and key workflow contracts')

if __name__=='__main__':
    try: run()
    except Exception as exc:
        print('FAIL:',exc,file=sys.stderr);sys.exit(1)
