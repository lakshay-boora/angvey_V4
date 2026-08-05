"""Angvey V4 command-line interface."""

from __future__ import annotations

import click
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from angvey import __version__

console = Console()


@click.group()
@click.version_option(__version__, prog_name="angvey")
def cli() -> None:
    """Angvey V4 — Personal AI agent that thinks, decides, and delivers real automations."""


@cli.command()
def init() -> None:
    """Interactive setup wizard. Creates ~/.angvey/config.json"""
    console.print(
        Panel(
            "[bold cyan]Angvey V4[/bold cyan] — Setup Wizard",
            border_style="cyan",
            padding=(0, 1),
        )
    )
    console.print()
    console.print("[dim]This wizard will help you configure your first provider and workspace.[/dim]")
    console.print("[dim]Full interactive setup coming in the next release.[/dim]")
    console.print()
    console.print("For now, copy the example config:")
    console.print("  [cyan]mkdir -p ~/.angvey && cp config.example.json ~/.angvey/config.json[/cyan]")
    console.print()
    console.print("Then edit ~/.angvey/config.json and run:")
    console.print("  [cyan]angvey chat[/cyan]")


@cli.command()
@click.option("-m", "--message", default=None, help="Single message (non-interactive).")
@click.option("-v", "--verbose", is_flag=True, help="Show debug logs.")
@click.option("-s", "--session", default=None, help="Resume a session by ID.")
def chat(message: str | None, verbose: bool, session: str | None) -> None:
    """Start an interactive chat session with Angvey."""
    header = Text()
    header.append("Angvey V4", style="bold cyan")
    header.append(f" v{__version__}", style="dim")
    header.append("  •  Your personal AI agent", style="dim")
    console.print(Panel(header, border_style="cyan", padding=(0, 1)))
    console.print()

    if message:
        console.print(f"[bold]You:[/bold] {message}")
        console.print("[dim]Agent loop not fully wired yet — core scaffold is ready.[/dim]")
        return

    console.print("[dim]Interactive mode placeholder.[/dim]")
    console.print("[dim]Core agent loop, tools, memory and providers are being built.[/dim]")
    console.print()
    console.print("Type [cyan]/help[/cyan] for commands once the full loop is live.")


@cli.command()
def status() -> None:
    """Show current configuration and status."""
    console.print("[bold cyan]Angvey V4 Status[/bold cyan]")
    console.print(f"Version : {__version__}")
    console.print("Config  : ~/.angvey/config.json (expected)")
    console.print("Status  : Scaffold ready — agent loop coming next")


if __name__ == "__main__":
    cli()
