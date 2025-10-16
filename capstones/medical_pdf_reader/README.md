# Capstone 1: Medical PDF Reader

A didactic medical document reader that uses AI to extract, summarize, and answer questions about medical literature.

## Features

- **PDF Processing**: Extract text and structure from medical PDFs
- **Semantic Search**: Find relevant sections in medical documents
- **Question Answering**: Answer questions about medical content
- **Summarization**: Generate summaries of medical papers
- **Multi-Modal**: Support for text, images, and tables
- **Guardrails**: Medical safety checks and disclaimers

## Architecture

```
┌─────────────┐
│   PDF Input │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Extractor  │ → Text, Images, Tables
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Embeddings │ → Vector Store
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    Agent    │ → Medical QA
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Guardrails │ → Safety Checks
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Response  │
└─────────────┘
```

## Prerequisites

- Completed all four modules (SDKs, MCP, Agents, AgentKit)
- Understanding of PDF processing
- Knowledge of embeddings and vector stores

## Getting Started

```bash
# Install dependencies
make bootstrap

# Run the application
make capstone-medical

# Or directly
cd capstones/medical_pdf_reader
python main.py
```

## Usage

```python
from medical_pdf_reader import MedicalPDFReader

reader = MedicalPDFReader()

# Load a PDF
reader.load_pdf("path/to/medical_paper.pdf")

# Ask questions
answer = reader.ask("What are the main findings?")
print(answer)

# Get summary
summary = reader.summarize()
print(summary)
```

## Configuration

Configure in `.env`:
- `MEDICAL_PDF_PATH`: Path to medical documents
- Medical safety guardrails settings
- Model selection for medical domain

## Safety Notes

⚠️ **Important**: This is an educational tool. Always consult qualified healthcare professionals for medical advice. The application includes safety disclaimers with all responses.
