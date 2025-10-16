"""
Medical PDF Reader - Capstone Project
A didactic tool for reading and analyzing medical documents.
"""

import os
from pathlib import Path
from typing import List, Optional

from rich.console import Console
from rich.panel import Panel

console = Console()


class MedicalPDFReader:
    """
    Medical PDF Reader for educational purposes.
    
    WARNING: This is an educational tool. Always consult qualified
    healthcare professionals for medical advice.
    """
    
    def __init__(self):
        """Initialize the Medical PDF Reader."""
        self.pdf_path = os.getenv("MEDICAL_PDF_PATH", "./data/medical_docs/")
        self.documents = []
        
        console.print(
            Panel(
                "[yellow]⚠️  EDUCATIONAL TOOL ONLY[/yellow]\n\n"
                "This application is for learning purposes.\n"
                "Always consult qualified healthcare professionals.",
                title="Medical Disclaimer",
                border_style="yellow"
            )
        )
    
    def load_pdf(self, filepath: str):
        """
        Load a medical PDF document.
        
        TODO: Implement PDF loading using PyPDF or PyMuPDF
        """
        console.print(f"[blue]Loading PDF: {filepath}[/blue]")
        # TODO: Implement PDF loading
        pass
    
    def extract_text(self) -> str:
        """
        Extract text from loaded PDF.
        
        TODO: Implement text extraction
        """
        # TODO: Implement text extraction
        pass
    
    def chunk_text(self, text: str, chunk_size: int = 1000) -> List[str]:
        """
        Chunk text for processing.
        
        TODO: Implement intelligent chunking that respects sections
        """
        # TODO: Implement chunking
        pass
    
    def create_embeddings(self, chunks: List[str]):
        """
        Create embeddings for text chunks.
        
        TODO: Implement embedding creation and vector store
        """
        # TODO: Implement embeddings
        pass
    
    def ask(self, question: str) -> str:
        """
        Ask a question about the medical document.
        
        TODO: Implement RAG-based question answering with guardrails
        """
        console.print(f"\n[bold blue]Question:[/bold blue] {question}")
        
        # TODO: Implement question answering
        
        disclaimer = "\n\n⚠️ This is an educational response. Consult healthcare professionals."
        return "Not implemented yet" + disclaimer
    
    def summarize(self) -> str:
        """
        Generate a summary of the medical document.
        
        TODO: Implement summarization with medical context
        """
        # TODO: Implement summarization
        return "Not implemented yet"


def main():
    """Main application entry point."""
    console.print("\n[bold blue]🏥 Medical PDF Reader[/bold blue]\n")
    
    reader = MedicalPDFReader()
    
    # Demo usage
    console.print("[dim]Demo mode - implement the full functionality in the labs[/dim]\n")
    
    # Check if sample PDFs exist
    sample_dir = Path("./data/medical_docs")
    if sample_dir.exists():
        pdfs = list(sample_dir.glob("*.pdf"))
        if pdfs:
            console.print(f"[green]Found {len(pdfs)} PDF(s) in {sample_dir}[/green]")
            for pdf in pdfs:
                console.print(f"  • {pdf.name}")
        else:
            console.print(f"[yellow]No PDFs found in {sample_dir}[/yellow]")
    else:
        console.print(f"[yellow]Directory {sample_dir} does not exist[/yellow]")
        console.print("[dim]Create it and add medical PDFs to test[/dim]")
    
    console.print("\n[bold green]✓ Application ready[/bold green]")
    console.print("[dim]Implement the TODOs to complete the capstone[/dim]\n")


if __name__ == "__main__":
    main()
