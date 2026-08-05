"""Configuration loading and defaults for Angvey V4."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


DEFAULT_CONFIG_PATH = Path.home() / ".angvey" / "config.json"


@dataclass
class ProviderConfig:
    base_url: str = ""
    api_key: str = ""
    model: str = ""
    think: bool | str = False


@dataclass
class AgentConfig:
    max_iterations: int = 25
    temperature: float = 0.7
    system_prompt: str = ""


@dataclass
class ToolsConfig:
    sandbox_level: str = "workspace"  # unrestricted | workspace | readonly
    blocked_commands: list[str] = field(default_factory=lambda: ["rm -rf /", "sudo", "mkfs"])


@dataclass
class MemoryConfig:
    enabled: bool = True
    max_entries: int = 2000


@dataclass
class Config:
    provider: str = "ollama"
    providers: dict[str, ProviderConfig] = field(default_factory=dict)
    agent: AgentConfig = field(default_factory=AgentConfig)
    tools: ToolsConfig = field(default_factory=ToolsConfig)
    memory: MemoryConfig = field(default_factory=MemoryConfig)
    workspace: str = "~/.angvey/workspace"

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Config":
        providers: dict[str, ProviderConfig] = {}
        for name, p in data.get("providers", {}).items():
            providers[name] = ProviderConfig(
                base_url=p.get("baseUrl", ""),
                api_key=p.get("apiKey", ""),
                model=p.get("model", ""),
                think=p.get("think", False),
            )

        agent_data = data.get("agent", {})
        tools_data = data.get("tools", {})
        memory_data = data.get("memory", {})

        return cls(
            provider=data.get("provider", "ollama"),
            providers=providers,
            agent=AgentConfig(
                max_iterations=agent_data.get("maxIterations", 25),
                temperature=agent_data.get("temperature", 0.7),
                system_prompt=agent_data.get("systemPrompt", ""),
            ),
            tools=ToolsConfig(
                sandbox_level=tools_data.get("sandboxLevel", "workspace"),
                blocked_commands=tools_data.get("blockedCommands", ["rm -rf /", "sudo", "mkfs"]),
            ),
            memory=MemoryConfig(
                enabled=memory_data.get("enabled", True),
                max_entries=memory_data.get("maxEntries", 2000),
            ),
            workspace=data.get("workspace", "~/.angvey/workspace"),
        )


def load_config(path: Path | None = None) -> Config:
    """Load config from disk or return sensible defaults."""
    cfg_path = path or DEFAULT_CONFIG_PATH
    if not cfg_path.exists():
        return Config()
    with open(cfg_path, encoding="utf-8") as f:
        data = json.load(f)
    return Config.from_dict(data)
