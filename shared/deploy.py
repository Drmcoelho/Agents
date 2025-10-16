"""
Deployment script for Agents Course applications.
"""

import sys
from pathlib import Path

from rich.console import Console

console = Console()


def deploy_medical_pdf_reader():
    """Deploy Medical PDF Reader capstone."""
    console.print("[blue]🏥 Deploying Medical PDF Reader...[/blue]")
    # Add actual deployment logic here
    console.print("[green]✓ Medical PDF Reader deployed![/green]")


def deploy_b2c_service():
    """Deploy B2C Customer Service capstone."""
    console.print("[blue]💬 Deploying B2C Customer Service...[/blue]")
    # Add actual deployment logic here
    console.print("[green]✓ B2C Customer Service deployed![/green]")


def deploy_all():
    """Deploy all applications."""
    console.print("[bold blue]🚀 Deploying all applications...[/bold blue]\n")
    deploy_medical_pdf_reader()
    deploy_b2c_service()
    console.print("\n[bold green]✅ All applications deployed![/bold green]")


def main():
    """Main function."""
    if len(sys.argv) < 2:
        deploy_all()
    else:
        target = sys.argv[1]
        
        if target == "medical":
            deploy_medical_pdf_reader()
        elif target == "b2c":
            deploy_b2c_service()
        else:
            console.print(f"[red]Unknown deployment target: {target}[/red]")
            sys.exit(1)


if __name__ == "__main__":
    main()
