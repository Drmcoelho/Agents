# py/server.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any, List

app = FastAPI(
    title="Servidor de Ferramentas MCP",
    description="Um servidor simples que expõe ferramentas para um agente de IA.",
)

# --- Modelos de Dados (Pydantic) ---

class ToolSchema(BaseModel):
    """Descreve a estrutura de uma ferramenta."""
    name: str
    description: str
    parameters: Dict[str, Any]

class InvokeRequest(BaseModel):
    """Modelo para a requisição de invocação de ferramenta."""
    tool_name: str
    arguments: Dict[str, Any]

class InvokeResponse(BaseModel):
    """Modelo para a resposta da invocação."""
    result: Any

# --- Banco de Dados Simulado de Ferramentas ---

TOOLS_DB = [
    {
        "name": "calculator",
        "description": "Calcula uma expressão matemática. Suporta operações básicas: +, -, *, /, parênteses e potenciação (**)",
        "parameters": {
            "expression": {
                "type": "string",
                "description": "A expressão matemática a ser calculada (ex: '2 * (3 + 4)')"
            }
        }
    },
    {
        "name": "text_analyzer",
        "description": "Analisa um texto e retorna estatísticas básicas como número de palavras e caracteres.",
        "parameters": {
            "text": {
                "type": "string",
                "description": "O texto a ser analisado"
            }
        }
    }
]

# --- Lógica das Ferramentas ---

def calculator(expression: str) -> float:
    """Executa uma expressão matemática."""
    # CUIDADO: eval() não é seguro em produção! Usado aqui para simplicidade.
    try:
        # Validação básica de segurança: permitir apenas caracteres seguros
        allowed_chars = set("0123456789+-*/()%. ")
        if not all(c in allowed_chars for c in expression):
            return "Erro: Expressão contém caracteres não permitidos"
        
        # Avalia a expressão matemática
        result = eval(expression)
        return float(result)
    except Exception as e:
        return f"Erro ao calcular: {e}"

def text_analyzer(text: str) -> Dict[str, int]:
    """Analisa um texto e retorna o número de palavras e caracteres."""
    # Conta caracteres (incluindo espaços)
    char_count = len(text)
    
    # Conta palavras (separadas por espaços)
    word_count = len(text.split()) if text.strip() else 0
    
    return {
        "word_count": word_count,
        "char_count": char_count
    }

# Mapeamento de nomes de ferramentas para suas funções
TOOL_FUNCTIONS = {
    "calculator": calculator,
    "text_analyzer": text_analyzer,
}

# --- Endpoints da API ---

@app.get("/tools", response_model=List[ToolSchema])
def list_tools():
    """
    Endpoint de descoberta.
    Retorna a lista de ferramentas disponíveis neste servidor.
    """
    return TOOLS_DB

@app.post("/invoke", response_model=InvokeResponse)
def invoke_tool(request: InvokeRequest):
    """
    Endpoint de invocação.
    Executa uma ferramenta com base no nome e nos argumentos fornecidos.
    """
    tool_name = request.tool_name
    arguments = request.arguments

    # Verifica se a ferramenta existe
    if tool_name not in TOOL_FUNCTIONS:
        return InvokeResponse(
            result=f"Erro: Ferramenta '{tool_name}' não encontrada. Ferramentas disponíveis: {list(TOOL_FUNCTIONS.keys())}"
        )
    
    # Obtém a função da ferramenta
    tool_function = TOOL_FUNCTIONS[tool_name]
    
    try:
        # Chama a função com os argumentos fornecidos
        result = tool_function(**arguments)
        return InvokeResponse(result=result)
    except TypeError as e:
        return InvokeResponse(
            result=f"Erro: Argumentos inválidos para a ferramenta '{tool_name}'. Detalhes: {e}"
        )
    except Exception as e:
        return InvokeResponse(
            result=f"Erro ao executar ferramenta '{tool_name}': {e}"
        )
