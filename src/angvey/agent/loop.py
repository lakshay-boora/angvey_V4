"""ReAct-style agent loop for Angvey V4.

The loop follows the classic pattern:
  Think → Act (tool call) → Observe → repeat until final answer.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Awaitable


@dataclass
class Message:
    role: str  # system | user | assistant | tool
    content: str
    tool_call_id: str | None = None
    name: str | None = None


@dataclass
class ToolCall:
    id: str
    name: str
    arguments: dict[str, Any]


@dataclass
class AgentResult:
    final_answer: str
    messages: list[Message] = field(default_factory=list)
    iterations: int = 0
    tool_calls: int = 0


class AgentLoop:
    """Minimal ReAct agent loop.

    This is the core orchestration skeleton. Providers, tools and memory
    plug into this class. Full implementation will grow here.
    """

    def __init__(
        self,
        *,
        max_iterations: int = 25,
        system_prompt: str = "",
        tools: dict[str, Callable[..., Awaitable[str]]] | None = None,
    ) -> None:
        self.max_iterations = max_iterations
        self.system_prompt = system_prompt or self._default_system_prompt()
        self.tools = tools or {}
        self.messages: list[Message] = []

    def _default_system_prompt(self) -> str:
        return (
            "You are Angvey, a personal AI agent that thinks, decides, "
            "and delivers real automations. You use tools when needed, "
            "keep answers clear and actionable, and prefer concrete results "
            "over vague advice."
        )

    async def run(self, user_message: str) -> AgentResult:
        """Run the agent until it produces a final answer or hits the iteration limit."""
        self.messages = [
            Message(role="system", content=self.system_prompt),
            Message(role="user", content=user_message),
        ]

        # Placeholder: full LLM + tool-calling loop will be implemented next.
        # For now we return a transparent status so the scaffold is usable.
        answer = (
            "Angvey V4 core loop is ready. "
            "Connect a provider and tools to unlock full automation."
        )
        self.messages.append(Message(role="assistant", content=answer))

        return AgentResult(
            final_answer=answer,
            messages=list(self.messages),
            iterations=1,
            tool_calls=0,
        )
