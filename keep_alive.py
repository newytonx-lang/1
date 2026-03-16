import os
import threading
import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", 10000))

class Handler(BaseHTTPRequestHandler):
    def _send_ok(self, with_body=False):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        if with_body:
            self.wfile.write(b"OK")

    def do_GET(self):
        self._send_ok(with_body=True)

    def do_HEAD(self):
        self._send_ok(with_body=False)

    def log_message(self, format, *args):
        return

def run_web():
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Keep-alive server running on port {PORT}")
    server.serve_forever()

def run_bot():
    subprocess.run(["python3", "modules/main.py"])

if __name__ == "__main__":
    t = threading.Thread(target=run_web, daemon=True)
    t.start()
    run_bot()
