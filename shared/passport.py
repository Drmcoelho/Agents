"""
Passport System for Progress Tracking.
Tracks student progress through the course modules and labs.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

from rich.console import Console
from rich.panel import Panel
from rich.progress import BarColumn, Progress, TextColumn
from rich.table import Table
from rich.tree import Tree

console = Console()


class Passport:
    """Progress passport manager."""
    
    def __init__(self, passport_file: str = ".passport.json"):
        self.passport_file = Path(passport_file)
        self.data = self.load()
    
    def load(self) -> Dict:
        """Load passport data."""
        if not self.passport_file.exists():
            return self.create_new()
        
        with open(self.passport_file) as f:
            return json.load(f)
    
    def save(self):
        """Save passport data."""
        with open(self.passport_file, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def create_new(self) -> Dict:
        """Create new passport."""
        return {
            "created_at": datetime.now().isoformat(),
            "last_updated": datetime.now().isoformat(),
            "modules": {
                "sdks": {
                    "status": "not_started",
                    "labs_completed": [],
                    "progress": 0,
                },
                "mcp": {
                    "status": "not_started",
                    "labs_completed": [],
                    "progress": 0,
                },
                "agents": {
                    "status": "not_started",
                    "labs_completed": [],
                    "progress": 0,
                },
                "agentkit": {
                    "status": "not_started",
                    "labs_completed": [],
                    "progress": 0,
                },
            },
            "capstones": {
                "medical_pdf_reader": {
                    "status": "locked",
                    "completed": False,
                },
                "b2c_service": {
                    "status": "locked",
                    "completed": False,
                },
            },
            "achievements": [],
        }
    
    def update_lab_completion(self, module: str, lab: str):
        """Mark a lab as completed."""
        if module not in self.data["modules"]:
            console.print(f"[red]Unknown module: {module}[/red]")
            return
        
        if lab not in self.data["modules"][module]["labs_completed"]:
            self.data["modules"][module]["labs_completed"].append(lab)
            self.data["last_updated"] = datetime.now().isoformat()
            
            # Update status
            if self.data["modules"][module]["status"] == "not_started":
                self.data["modules"][module]["status"] = "in_progress"
            
            self.save()
            console.print(f"[green]✓ Lab {lab} completed in {module}![/green]")
    
    def get_overall_progress(self) -> float:
        """Calculate overall progress percentage."""
        total_progress = sum(
            m["progress"] for m in self.data["modules"].values()
        )
        return total_progress / len(self.data["modules"])
    
    def display(self):
        """Display passport with progress."""
        console.print("\n[bold blue]🎫 Your Progress Passport[/bold blue]\n")
        
        # Created date
        created = datetime.fromisoformat(self.data["created_at"])
        console.print(f"[dim]Created: {created.strftime('%Y-%m-%d %H:%M')}[/dim]")
        
        updated = datetime.fromisoformat(self.data["last_updated"])
        console.print(f"[dim]Last Updated: {updated.strftime('%Y-%m-%d %H:%M')}[/dim]\n")
        
        # Modules progress
        tree = Tree("[bold]Course Modules[/bold]")
        
        for module, info in self.data["modules"].items():
            status = info["status"]
            progress = info["progress"]
            labs_count = len(info["labs_completed"])
            
            status_icon = {
                "not_started": "⭘",
                "in_progress": "◐",
                "completed": "✓",
            }.get(status, "?")
            
            status_color = {
                "not_started": "dim",
                "in_progress": "yellow",
                "completed": "green",
            }.get(status, "white")
            
            module_branch = tree.add(
                f"[{status_color}]{status_icon} {module.upper()}[/{status_color}] "
                f"- {progress}% ({labs_count} labs)"
            )
            
            for lab in info["labs_completed"]:
                module_branch.add(f"[green]✓[/green] {lab}")
        
        console.print(tree)
        console.print()
        
        # Capstones
        console.print("[bold]🎓 Capstone Projects[/bold]\n")
        
        for capstone, info in self.data["capstones"].items():
            status = info["status"]
            completed = info["completed"]
            
            if completed:
                icon = "✓"
                color = "green"
            elif status == "locked":
                icon = "🔒"
                color = "dim"
            else:
                icon = "◐"
                color = "yellow"
            
            console.print(
                f"  [{color}]{icon} {capstone.replace('_', ' ').title()}[/{color}]"
            )
        
        console.print()
        
        # Overall progress bar
        overall_progress = self.get_overall_progress()
        
        console.print("[bold]Overall Progress[/bold]\n")
        
        with Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=console,
        ) as progress:
            task = progress.add_task("", total=100, completed=overall_progress)
        
        console.print()
        
        # Achievements
        if self.data["achievements"]:
            console.print("[bold]🏆 Achievements[/bold]\n")
            for achievement in self.data["achievements"]:
                console.print(f"  [yellow]★[/yellow] {achievement}")
            console.print()
    
    def unlock_capstone(self, capstone: str):
        """Unlock a capstone project."""
        if capstone in self.data["capstones"]:
            self.data["capstones"][capstone]["status"] = "unlocked"
            self.data["last_updated"] = datetime.now().isoformat()
            self.save()
            console.print(f"[green]✓ Capstone {capstone} unlocked![/green]")
    
    def complete_capstone(self, capstone: str):
        """Mark a capstone as completed."""
        if capstone in self.data["capstones"]:
            self.data["capstones"][capstone]["completed"] = True
            self.data["capstones"][capstone]["status"] = "completed"
            self.data["last_updated"] = datetime.now().isoformat()
            
            # Add achievement
            achievement = f"Completed {capstone.replace('_', ' ').title()}"
            if achievement not in self.data["achievements"]:
                self.data["achievements"].append(achievement)
            
            self.save()
            console.print(f"[bold green]🎉 Capstone {capstone} completed![/bold green]")


def main():
    """Main function."""
    passport = Passport()
    passport.display()


if __name__ == "__main__":
    main()
