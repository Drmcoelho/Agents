"""
Environment configuration checker for Agents Course.
Validates that all required environment variables are set.
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple

from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table

console = Console()

# Load environment variables
load_dotenv()


def check_required_vars() -> Tuple[bool, List[str]]:
    """Check required environment variables."""
    required_vars = [
        "DEFAULT_BACKEND",
    ]
    
    missing = []
    for var in required_vars:
        if not os.getenv(var):
            missing.append(var)
    
    return len(missing) == 0, missing


def check_backend_config() -> Dict[str, bool]:
    """Check backend configurations."""
    backend = os.getenv("DEFAULT_BACKEND", "openai").lower()
    
    backends = {
        "openai": os.getenv("OPENAI_API_KEY", "").startswith("sk-"),
        "anthropic": bool(os.getenv("ANTHROPIC_API_KEY")),
        "google": bool(os.getenv("GOOGLE_API_KEY")),
    }
    
    return {
        "backend": backend,
        "configured": backends.get(backend, False),
        "all_backends": backends,
    }


def display_status():
    """Display environment status."""
    console.print("\n[bold blue]🔍 Environment Configuration Status[/bold blue]\n")
    
    # Check required vars
    all_ok, missing = check_required_vars()
    
    if missing:
        console.print("[yellow]⚠️  Missing required variables:[/yellow]")
        for var in missing:
            console.print(f"  • {var}")
        console.print()
    
    # Check backends
    backend_info = check_backend_config()
    
    table = Table(title="AI Backend Configuration")
    table.add_column("Backend", style="cyan")
    table.add_column("Status", style="green")
    table.add_column("Selected", style="yellow")
    
    for backend, configured in backend_info["all_backends"].items():
        status = "✓ Configured" if configured else "✗ Not configured"
        selected = "●" if backend == backend_info["backend"] else ""
        table.add_row(backend.upper(), status, selected)
    
    console.print(table)
    console.print()
    
    # Overall status
    if backend_info["configured"]:
        console.print("[bold green]✅ Selected backend is properly configured![/bold green]\n")
        return True
    else:
        console.print(
            f"[bold red]❌ Selected backend '{backend_info['backend']}' is not configured![/bold red]"
        )
        console.print(
            "[yellow]Please add the appropriate API key to your .env file.[/yellow]\n"
        )
        return False


def main():
    """Main function."""
    if not Path(".env").exists():
        console.print(
            "[bold red]❌ .env file not found![/bold red]"
        )
        console.print(
            "[yellow]Run 'make bootstrap' to create it from .env.example[/yellow]\n"
        )
        sys.exit(1)
    
    if not display_status():
        sys.exit(1)


if __name__ == "__main__":
    main()
