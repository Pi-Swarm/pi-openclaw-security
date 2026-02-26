# 🛡️ Pi-OpenClaw Security Edition

**Enhanced OpenClaw with Security Tools for Sovereign AI**

Pi-OpenClaw Security is a Node.js wrapper that extends OpenClaw with specialized security auditing capabilities. Built for Pi Swarm's autonomous security operations.

---

## ⚡ Features

- 🔍 **Security Auditing** - Automated code vulnerability detection
- 🌐 **API Leak Detection** - Find exposed secrets and PII
- 📱 **Network Scanning** - Integrated nmap for reconnaissance
- 🤖 **AI-Powered** - Enhanced prompts for security analysis
- 🦀 **Rust Core Ready** - Compatible with Pi-Swarm Rust binaries

---

## 📦 Installation

### Prerequisites
```bash
# Node.js 18+ required
node --version

# OpenClaw must be installed
npm install -g openclaw
```

### Clone and Setup
```bash
# Clone repository
git clone https://github.com/Pi-Swarm/pi-openclaw-security.git
cd pi-openclaw-security

# Install dependencies
npm install

# Link globally (optional)
npm link
```

---

## 🎮 How to Run

### 1. Basic Security Commands

```bash
# Check system status
pi-security status

# Run security audit on code
pi-security audit ./src/index.js

# Audit a GitHub repository
pi-security audit https://github.com/user/repo

# Network scan
pi-security scan 192.168.1.1

# Interactive security agent
pi-security agent "Find SQL injection vulnerabilities"
```

### 2. Development Mode

```bash
# Run in development
npm run dev

# Run tests
npm test

# Build for production
npm run build
```

### 3. Integration with OpenClaw

```bash
# pi-security extends openclaw commands
pi-security --help

# Example: Secure audit with AI analysis
pi-security audit ./smart_contract.sol --ai-enhanced
```

---

## 🔧 Configuration

### Environment Variables
```bash
# AI Model configuration
export PI_MODEL="qwen2.5:1.5b"
export PI_OLLAMA_URL="http://localhost:11434"

# Security settings
export PI_SECURITY_LEVEL="high"
export PI_AUDIT_DEEP="true"

# Telegram notifications (optional)
export PI_TELEGRAM_TOKEN="your_bot_token"
```

### Config File
Create `~/.pi-security/config.json`:
```json
{
  "model": "qwen2.5:1.5b",
  "securityLevel": "high",
  "autoFix": false,
  "notifications": {
    "telegram": false
  }
}
```

---

## 🛠️ Security Tools

### Available Commands

| Command | Description | Example |
|---------|-------------|---------|
| `audit` | Code security audit | `pi-security audit ./file.js` |
| `scan` | Network port scan | `pi-security scan 192.168.1.1` |
| `agent` | AI security chat | `pi-security agent "Check for XSS"` |
| `status` | System health check | `pi-security status` |
| `patch` | Auto-fix vulnerabilities | `pi-security patch ./file.js` |

---

## 🔄 Workflow Examples

### Smart Contract Audit
```bash
# Audit Solana/Rust contract
pi-security audit ./programs/src/lib.rs

# With AI explanation
pi-security audit ./contract.sol --explain
```

### API Security Test
```bash
# Test API for vulnerabilities
pi-security scan-api https://api.example.com

# Check for exposed secrets
pi-security audit-repo https://github.com/user/repo
```

### Continuous Monitoring
```bash
# Set up watch mode
pi-security watch ./src --on-change audit

# Run daemon
pi-security daemon --port 18789
```

---

## 🐛 Troubleshooting

### Issue: OpenClaw not found
```bash
# Install OpenClaw first
npm install -g openclaw

# Or verify path
which openclaw
```

### Issue: Ollama not connected
```bash
# Start Ollama
ollama serve

# Pull required model
ollama pull qwen2.5:1.5b
```

### Issue: Permission denied
```bash
# Fix permissions
chmod +x ./bin/pi-security

# Or use npx
npx pi-security status
```

---

## 🚀 Deployment

### Docker
```dockerfile
FROM node:18-alpine
RUN npm install -g openclaw pi-openclaw-security
CMD ["pi-security", "daemon"]
```

### Systemd Service
```ini
[Unit]
Description=Pi-OpenClaw Security Daemon
After=network.target

[Service]
ExecStart=/usr/bin/pi-security daemon
Restart=always
User=pi-swarm

[Install]
WantedBy=multi-user.target
```

---

## 📞 Support

- **Issues**: https://github.com/Pi-Swarm/pi-openclaw-security/issues
- **Documentation**: See README.md in repository
- **Security Reports**: security@pi-swarm.local

---

**🛡️ Sovereign AI Security. Powered by OpenClaw.**
