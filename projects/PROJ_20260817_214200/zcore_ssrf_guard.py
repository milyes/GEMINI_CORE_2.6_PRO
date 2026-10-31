import ipaddress
import json
import time
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler

IMDS_IP = ipaddress.ip_address("169.254.169.254")
BLOCKED_PAYLOADS = ["169.254.169.254", "::ffff:169.254.169.254"]
PORT = 8000

def canonicalize_ip(url: str) -> str:
    try:
        if "::ffff:" in url:
            ip_part = url.split("::ffff:")[1].split("/")[0].split(":")[0]
            return ip_part
    except:
        pass
    return url

def detect_ssrf(url: str) -> dict:
    start = time.time()
    canonical = canonicalize_ip(url)
    blocked = False
    
    try:
        ip = ipaddress.ip_address(canonical)
        if ip == IMDS_IP:
            blocked = True
    except:
        for payload in BLOCKED_PAYLOADS:
            if payload in url:
                blocked = True
                break
    
    latency = round((time.time() - start) * 1000, 4)
    
    result = {
        "timestamp": datetime.utcnow().isoformat(),
        "payload": url,
        "canonical": canonical,
        "blocked": blocked,
        "latency_ms": latency,
        "reason": "IMDS Block" if blocked else "Clean"
    }
    print(json.dumps(result))
    return result

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/scan":
            length = int(self.headers['Content-Length'])
            data = json.loads(self.rfile.read(length))
            url = data.get("url", "")
            result = detect_ssrf(url)
            status = 403 if result["blocked"] else 200
            self.send_response(status)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "Z-CORE v10.2.1 Online", "mode": "Zero-Trust Local"}')
        else:
            self.send_response(404)
            self.end_headers()
    
    def log_message(self, format, *args):
        return

if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', PORT), Handler)
    print(f"[Z-CORE] Serveur démarré sur port {PORT} - Zero-Trust Local")
    server.serve_forever()
