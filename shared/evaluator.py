"""
Evaluator for Agents Course.
Runs evaluations to assess student progress across all modules.
"""

import json
import subprocess
from pathlib import Path
from typing import Dict, List

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table

console = Console()


class Evaluator:
    """Course evaluator."""
    
    def __init__(self):
        self.modules = ["sdks", "mcp", "agents", "agentkit"]
        self.results = {}
    
    def run_module_tests(self, module: str) -> Dict:
        """Run tests for a specific module."""
        console.print(f"\n[blue]Running tests for {module}...[/blue]")
        
        module_path = Path(module)
        labs_path = module_path / "labs"
        tests_path = module_path / "tests"
        
        if not tests_path.exists():
            return {
                "status": "skipped",
                "message": "No tests found",
                "passed": 0,
                "total": 0,
            }
        
        try:
            result = subprocess.run(
                [
                    "python", "-m", "pytest",
                    str(tests_path),
                    "-v",
                    "--tb=short",
                    "--json-report",
                    "--json-report-file=/tmp/pytest_report.json",
                ],
                capture_output=True,
                text=True,
                timeout=60,
            )
            
            # Try to load JSON report
            report_path = Path("/tmp/pytest_report.json")
            if report_path.exists():
                with open(report_path) as f:
                    report = json.load(f)
                    
                return {
                    "status": "passed" if result.returncode == 0 else "failed",
                    "passed": report.get("summary", {}).get("passed", 0),
                    "total": report.get("summary", {}).get("total", 0),
                    "duration": report.get("duration", 0),
                }
            else:
                # Fallback to parsing output
                passed = result.returncode == 0
                return {
                    "status": "passed" if passed else "failed",
                    "passed": 0,
                    "total": 0,
                    "output": result.stdout,
                }
        
        except subprocess.TimeoutExpired:
            return {
                "status": "timeout",
                "message": "Tests timed out",
                "passed": 0,
                "total": 0,
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e),
                "passed": 0,
                "total": 0,
            }
    
    def evaluate_all(self):
        """Evaluate all modules."""
        console.print("\n[bold blue]📊 Running Course Evaluations[/bold blue]\n")
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            for module in self.modules:
                task = progress.add_task(f"Evaluating {module}...", total=None)
                self.results[module] = self.run_module_tests(module)
                progress.remove_task(task)
        
        self.display_results()
        self.save_results()
    
    def display_results(self):
        """Display evaluation results."""
        console.print("\n[bold blue]📈 Evaluation Results[/bold blue]\n")
        
        table = Table(title="Module Test Results")
        table.add_column("Module", style="cyan")
        table.add_column("Status", style="green")
        table.add_column("Tests Passed", style="yellow")
        table.add_column("Duration (s)", style="magenta")
        
        for module, result in self.results.items():
            status = result.get("status", "unknown")
            
            if status == "passed":
                status_icon = "✓ Passed"
                status_style = "green"
            elif status == "failed":
                status_icon = "✗ Failed"
                status_style = "red"
            elif status == "skipped":
                status_icon = "- Skipped"
                status_style = "dim"
            else:
                status_icon = "? Unknown"
                status_style = "yellow"
            
            passed = result.get("passed", 0)
            total = result.get("total", 0)
            duration = result.get("duration", 0)
            
            table.add_row(
                module.upper(),
                f"[{status_style}]{status_icon}[/{status_style}]",
                f"{passed}/{total}" if total > 0 else "N/A",
                f"{duration:.2f}" if duration > 0 else "N/A",
            )
        
        console.print(table)
        console.print()
        
        # Calculate overall score
        total_passed = sum(r.get("passed", 0) for r in self.results.values())
        total_tests = sum(r.get("total", 0) for r in self.results.values())
        
        if total_tests > 0:
            score = (total_passed / total_tests) * 100
            console.print(f"[bold]Overall Score: {score:.1f}% ({total_passed}/{total_tests} tests passed)[/bold]\n")
    
    def save_results(self):
        """Save results to file."""
        results_path = Path(".eval_results.json")
        with open(results_path, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        console.print(f"[dim]Results saved to {results_path}[/dim]\n")


def main():
    """Main function."""
    evaluator = Evaluator()
    evaluator.evaluate_all()


if __name__ == "__main__":
    main()
