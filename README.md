# Angvey V4

**Your personal AI agent that thinks, decides, and delivers real automations.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen)](https://github.com/lakshay-boora/angvey_V4)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red)](https://github.com/lakshay-boora/angvey_V4)

> One instruction → Work gets done automatically.  
> Built for 2026 and beyond by **Angvey International**.

---

## What is Angvey V4?

Angvey V4 is an open-source personal AI agent runtime.  
It goes beyond chat: it reasons, plans multi-step workflows, uses tools, remembers context, and executes real automations — all while staying under your control.

**Design principles**
- Local-first & privacy-respecting
- Multi-provider (Ollama, OpenAI, any OpenAI-compatible endpoint)
- Clean, readable, contribution-friendly code
- Safe by default (sandbox levels + command blocklist)
- Extensible via plugins

---

## Features (current scaffold + roadmap)

| Area | Status |
|------|--------|
| ReAct agent loop | Scaffold ready |
| Multi-provider support | Planned (Ollama / OpenAI / local) |
| Built-in tools (shell, files, web, memory) | Registry ready |
| Persistent memory | Designed |
| Plugin system | Designed |
| Telegram channel | Optional |
| Sandbox levels | Configured |
| MCP support | Roadmap |
| Tool market / skill sharing | Roadmap |

---

## Quick Start

```bash
# Clone
git clone https://github.com/lakshay-boora/angvey_V4.git
cd angvey_V4

# Install (editable)
pip install -e .

# Copy example config
mkdir -p ~/.angvey
cp config.example.json ~/.angvey/config.json

# Run
angvey --help
angvey init
angvey chat
angvey status
```

> The core agent loop, providers and full tool handlers are being completed. The scaffold is already structured for rapid iteration.

---

## Project Structure

```
angvey_V4/
├── src/angvey/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py              # Click CLI (init, chat, status)
│   ├── config.py           # Typed configuration
│   └── agent/
│       ├── __init__.py
│       ├── loop.py         # ReAct agent loop
│       └── tools.py        # Built-in tool registry
├── config.example.json
├── pyproject.toml
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

---

## Configuration

See `config.example.json`. Key paths after setup:

- Config    → `~/.angvey/config.json`
- Workspace → `~/.angvey/workspace/`
- Memory    → `~/.angvey/memory.json`
- Plugins   → `~/.angvey/plugins/`

---

## Contributing

We welcome contributions of all kinds!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes
4. Push and open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

Copyright (c) 2026 lakshay-boora / Angvey International

---

## Open Source Credits & Acknowledgments

Angvey V4 stands on the shoulders of many excellent open-source projects.  
We gratefully acknowledge (non-exhaustive):

### Core & Runtime
- **Python** · **httpx** · **Click** · **Rich**

### AI / Agent Ecosystem
- **Model Context Protocol (MCP)**
- **Ollama** · **llama.cpp**
- **LangChain / LangGraph** (orchestration patterns)
- **OpenAI / Anthropic / Google / xAI SDKs**

### Inspiration & Related Agents
- **agent-mini** (clean local-first design)
- **Agenvoy** · **OpenHands** · **Aider** · **Continue**
- **Angy** · **MyAgentive** · **Aivy OS** and the wider open-source agent community

### Infrastructure
- **Docker / Podman** · **SQLite** · **Playwright** · **GitHub**

If you build on these projects, please respect their respective licenses.

---

## Roadmap

- [x] Professional open-source scaffold
- [x] CLI + config + agent loop skeleton
- [x] Tool registry
- [ ] Full provider implementations (Ollama, OpenAI, local)
- [ ] Real tool handlers + sandbox
- [ ] Persistent memory + sessions
- [ ] Plugin loader
- [ ] Telegram gateway
- [ ] MCP client/server
- [ ] Official launch (target: late 2026)

---

**Built with ❤️ by the Angvey team**  
Faridabad, Haryana · Angvey International

Star the repo if you believe personal AI should be open, private, and powerful.
