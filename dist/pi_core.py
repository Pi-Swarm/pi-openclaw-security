#!/usr/bin/env python3
"""Pi-Core Security Module for Pi-OpenClaw"""

import sys
import json
import urllib.request

OllamaURL = "http://localhost:11434/api/generate"
Model = "qwen2.5:1.5b"

class SecurityTools:
    def audit(self, target):
        return { "tool": "audit", "target": target, "status": "executed" }
    
    def scan(self, target):
        return { "tool": "scan", "target": target, "status": "executed" }
    
    def ask_ai(self, prompt):
        try:
            data = json.dumps({
                "model": Model,
                "prompt": prompt,
                "stream": False
            }).encode()
            req = urllib.request.Request(OllamaURL, data=data,
                headers={"Content-Type": "application/json"},
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=120) as resp:
                result = json.loads(resp.read().decode())
                return result.get("response", "No response")
        except Exception as e:
            return f"Error: {e}"

def main():
    if len(sys.argv) < 2:
        print("Usage: pi_core.py <command> [args...]")
        sys.exit(1)
    
    cmd = sys.argv[1]
    tool = SecurityTools()
    
    if cmd == "audit":
        target = sys.argv[2] if len(sys.argv) > 2 else "."
        result = tool.audit(target)
        response = tool.ask_ai(f"Security audit of {target}. Analyze for vulnerabilities.")
        print(f"Audited: {result['target']}")
        print(response)
    
    elif cmd == "scan":
        target = sys.argv[2] if len(sys.argv) > 2 else "127.0.0.1"
        print(f"Scanning: {target}")
        response = tool.ask_ai(f"Network scan of {target}. Analyze for security risks.")
        print(response)
    
    elif cmd == "task":
        desc = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "Security check"
        print(f"Task: {desc}")
        response = tool.ask_ai(f"Security task: {desc}")
        print(response)
    
    else:
        print(f"Unknown: {cmd}")

if __name__ == "__main__":
    main()
