# Angvey V4

**Your personal AI agent that thinks, decides, and delivers real automations.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Go](https://img.shields.io/badge/Go-1.22+-00ADD8?logo=go)](https://go.dev/)
[![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen)](https://github.com/lakshay-boora/angvey_V4)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red)](https://github.com/lakshay-boora/angvey_V4)

> One instruction → Work gets done automatically.  
> Built for 2026 and beyond by **Angvey International**.

---

## What is Angvey V4?

Angvey V4 is an open-source personal AI agent runtime.  
It goes beyond chat: it reasons, plans multi-step workflows, builds missing tools on the fly, remembers context, and executes real automations — all while staying under your control.

Key goals:
- Local-first / privacy-respecting where possible
- Multi-provider LLM support
- Self-improving tool generation
- Clean, auditable, contribution-friendly codebase

---

## Features

- **Autonomous tool creation** – Missing capabilities are generated, tested, and reused
- **Multi-step reasoning & planning**
- **Long-term memory & session management**
- **Scheduling & recurring automations**
- **MCP (Model Context Protocol) client & server support**
- **Multi-LLM providers** (Claude, OpenAI, Gemini, Grok, local models, etc.)
- **Sandbox execution** for safety
- **Extensible skill / plugin system**

---

## Quick Start

```bash
# Clone
git clone https://github.com/lakshay-boora/angvey_V4.git
cd angvey_V4

# Build (example)
make build   # or go build ./...

# Run
./angvey --help
```

> Detailed installation, configuration, and provider setup will be documented in `/docs` as the project matures.

---

## Project Structure (planned)

```
angvey_V4/
├── cmd/                 # CLI entrypoints
├── internal/            # Core agent logic
├── pkg/                 # Public packages
├── skills/              # Loadable skills
├── docs/                # Documentation
├── examples/            # Usage examples
├── LICENSE
└── README.md
```

---

## Contributing

We welcome contributions of all kinds!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

Please open an issue first for large changes.  
Code of Conduct and contribution guidelines will live in `CONTRIBUTING.md`.

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

Copyright (c) 2026 lakshay-boora / Angvey International

---

## Open Source Credits & Acknowledgments

Angvey V4 stands on the shoulders of many excellent open-source projects.  
We gratefully acknowledge the following (non-exhaustive list of libraries, frameworks, protocols, and tools commonly used or inspired by in this space):

### Core Runtime & Language
- **Go** – https://go.dev/ (The Go Programming Language)
- **bubblewrap / sandbox-exec** – Secure sandboxing on Linux/macOS

### AI / Agent Ecosystem
- **Model Context Protocol (MCP)** – Anthropic & community (https://modelcontextprotocol.io)
- **LangChain / LangGraph** – Inspiration for agent orchestration patterns
- **AutoGen / CrewAI / Semantic Kernel** – Multi-agent design ideas
- **OpenAI Python/Node SDKs**, **Anthropic SDK**, **Google Generative AI SDK**, **xAI Grok SDK**
- **Ollama** – Local model serving
- **llama.cpp / ggml** – Efficient local inference

### Tooling & Infrastructure
- **Cobra / Viper** – CLI and configuration (Go)
- **Bubble Tea / Lip Gloss** – Beautiful terminal UIs
- **Docker / Podman** – Containerized tool execution
- **cron / systemd timers** – Scheduling foundations
- **SQLite / DuckDB / KuraDB-style stores** – Lightweight memory & RAG
- **Playwright / Puppeteer** – Browser automation tools
- **pdftotext (poppler)** – Document parsing

### Protocols & Standards
- **OpenAPI / Swagger**
- **JSON Schema**
- **gRPC / Connect**
- **Server-Sent Events (SSE)** for streaming

### Inspiration & Related Open-Source Agents
- **Agenvoy** – Local AI agent that builds its own tools
- **OpenDevin / OpenHands**
- **SWE-agent**
- **Aider**
- **Continue.dev**
- **Cursor / Claude Code patterns** (open-source analogues)
- **Angy**, **MyAgentive**, **Aivy OS**, and many other community agent projects

### Documentation & Community
- **GitHub** – Hosting, issues, PRs, Actions
- **Markdown**, **MkDocs / Docusaurus** style documentation patterns
- All the individual maintainers and contributors of the projects listed above

If you use Angvey V4 and build on top of these projects, please also respect their respective licenses.

---

## Roadmap (high level)

- [ ] Stable core agent loop
- [ ] First-class MCP support
- [ ] Tool market / skill sharing
- [ ] Web dashboard
- [ ] Cross-platform installers
- [ ] Official launch (target: late 2026)

---

**Built with ❤️ by the Angvey team**  
Faridabad, Haryana · Angvey International

Star the repo if you believe personal AI should be open, private, and powerful.
