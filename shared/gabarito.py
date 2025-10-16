"""
Gabarito (Answer Key) System for Auto-Correction.
Provides automated correction and hints for lab exercises.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Optional

from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax

console = Console()


class Gabarito:
    """Answer key manager for auto-correction."""
    
    def __init__(self, module: str):
        self.module = module
        self.module_path = Path(module)
        self.gabarito_path = self.module_path / "gabarito.json"
        self.solutions_path = self.module_path / "solutions"
        
    def load_gabarito(self) -> Optional[Dict]:
        """Load the gabarito file."""
        if not self.gabarito_path.exists():
            console.print(
                f"[yellow]⚠️  No gabarito found for {self.module}[/yellow]"
            )
            return None
        
        with open(self.gabarito_path) as f:
            return json.load(f)
    
    def show_hints(self, exercise: str):
        """Show hints for an exercise."""
        gabarito = self.load_gabarito()
        if not gabarito or exercise not in gabarito:
            console.print(f"[red]❌ No hints available for {exercise}[/red]")
            return
        
        hints = gabarito[exercise].get("hints", [])
        console.print(f"\n[bold blue]💡 Hints for {exercise}:[/bold blue]\n")
        
        for i, hint in enumerate(hints, 1):
            console.print(f"[cyan]{i}.[/cyan] {hint}")
        console.print()
    
    def show_solution(self, exercise: str):
        """Show the solution for an exercise."""
        gabarito = self.load_gabarito()
        if not gabarito or exercise not in gabarito:
            console.print(f"[red]❌ No solution available for {exercise}[/red]")
            return
        
        solution_file = gabarito[exercise].get("solution_file")
        if not solution_file:
            console.print(f"[red]❌ No solution file specified for {exercise}[/red]")
            return
        
        solution_path = self.solutions_path / solution_file
        if not solution_path.exists():
            console.print(f"[red]❌ Solution file not found: {solution_path}[/red]")
            return
        
        console.print(f"\n[bold green]✓ Solution for {exercise}:[/bold green]\n")
        
        with open(solution_path) as f:
            code = f.read()
        
        syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
        console.print(Panel(syntax, title=f"Solution: {solution_file}"))
        console.print()
    
    def apply_fix(self, exercise: str, auto_apply: bool = False):
        """Apply automatic fix for an exercise."""
        gabarito = self.load_gabarito()
        if not gabarito or exercise not in gabarito:
            console.print(f"[red]❌ No fix available for {exercise}[/red]")
            return
        
        fix_info = gabarito[exercise]
        target_file = fix_info.get("target_file")
        
        if not target_file:
            console.print(f"[yellow]⚠️  No auto-fix available for {exercise}[/yellow]")
            self.show_solution(exercise)
            return
        
        target_path = self.module_path / target_file
        solution_file = fix_info.get("solution_file")
        solution_path = self.solutions_path / solution_file
        
        if not solution_path.exists():
            console.print(f"[red]❌ Solution file not found: {solution_path}[/red]")
            return
        
        console.print(f"\n[bold yellow]🔧 Applying fix for {exercise}...[/bold yellow]\n")
        
        if not auto_apply:
            response = console.input(
                f"[yellow]Replace {target_path} with solution? (y/n): [/yellow]"
            )
            if response.lower() != 'y':
                console.print("[yellow]Fix cancelled.[/yellow]")
                return
        
        # Create backup
        if target_path.exists():
            backup_path = target_path.with_suffix(target_path.suffix + '.bak')
            import shutil
            shutil.copy2(target_path, backup_path)
            console.print(f"[dim]Backup created: {backup_path}[/dim]")
        
        # Apply solution
        import shutil
        target_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(solution_path, target_path)
        
        console.print(f"[bold green]✅ Fix applied successfully![/bold green]\n")
    
    def list_exercises(self):
        """List all available exercises."""
        gabarito = self.load_gabarito()
        if not gabarito:
            return
        
        console.print(f"\n[bold blue]📚 Available exercises in {self.module}:[/bold blue]\n")
        
        for exercise, info in gabarito.items():
            console.print(f"[cyan]•[/cyan] {exercise}")
            if "description" in info:
                console.print(f"  {info['description']}")
        console.print()


def main():
    """Main function."""
    if len(sys.argv) < 2:
        console.print("[red]❌ Please specify a module[/red]")
        console.print("[yellow]Usage: python gabarito.py <module> [exercise][/yellow]")
        sys.exit(1)
    
    module = sys.argv[1]
    gabarito = Gabarito(module)
    
    if len(sys.argv) < 3:
        gabarito.list_exercises()
        sys.exit(0)
    
    exercise = sys.argv[2]
    
    console.print(f"\n[bold blue]🔧 Auto-correction for {module}/{exercise}[/bold blue]\n")
    
    # Show hints first
    gabarito.show_hints(exercise)
    
    # Ask if user wants to see solution
    response = console.input("[yellow]Show solution? (y/n): [/yellow]")
    if response.lower() == 'y':
        gabarito.show_solution(exercise)
    
    # Ask if user wants to apply fix
    response = console.input("[yellow]Apply automatic fix? (y/n): [/yellow]")
    if response.lower() == 'y':
        gabarito.apply_fix(exercise, auto_apply=False)


if __name__ == "__main__":
    main()
