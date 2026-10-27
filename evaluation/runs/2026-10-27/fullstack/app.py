from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import argparse
import json
import os
import tempfile
from threading import Lock
from uuid import uuid4

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "data" / "items.json"
DATA_LOCK = Lock()


def read_items():
    items = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    if not isinstance(items, list):
        raise ValueError("The device data must be an array")
    return items


def write_items(items):
    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=DATA_FILE.parent,
            prefix=".items-", suffix=".tmp", delete=False,
        ) as temporary_file:
            temporary_path = Path(temporary_file.name)
            json.dump(items, temporary_file, ensure_ascii=False, indent=2)
            temporary_file.write("\n")
            temporary_file.flush()
            os.fsync(temporary_file.fileno())
        temporary_path.replace(DATA_FILE)
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


class Handler(BaseHTTPRequestHandler):
    def send_json(self, status, payload):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/api/items":
            try:
                with DATA_LOCK:
                    items = read_items()
            except (OSError, ValueError):
                self.send_json(500, {"error": "storage_error"})
                return
            self.send_json(200, {"items": items})
        elif self.path == "/":
            body = (ROOT / "web" / "index.html").read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path != "/api/items":
            self.send_error(404)
            return

        try:
            content_length = int(self.headers.get("Content-Length", "0"))
            if content_length < 0:
                raise ValueError("Invalid content length")
            payload = json.loads(self.rfile.read(content_length).decode("utf-8"))
        except (ValueError, UnicodeError):
            self.send_json(400, {"error": "invalid_json"})
            return

        name = payload.get("name") if isinstance(payload, dict) else None
        if not isinstance(name, str) or not name.strip():
            self.send_json(400, {"error": "name_required"})
            return

        item = {"id": uuid4().hex, "name": name.strip()}
        try:
            with DATA_LOCK:
                items = read_items()
                items.append(item)
                write_items(items)
        except (OSError, ValueError):
            self.send_json(500, {"error": "storage_error"})
            return
        self.send_json(201, {"item": item})


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    ThreadingHTTPServer(("127.0.0.1", args.port), Handler).serve_forever()
