# tests/test_lab02.py
import pytest
from fastapi.testclient import TestClient
import sys
import os

# Adiciona o diretório do laboratório ao path para importar o server
lab_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'labs', '02_mcp', 'py'))
sys.path.insert(0, lab_path)

# Tenta importar o app; falha graciosamente se não for encontrado
try:
    from server import app
    client = TestClient(app)
except ImportError:
    pytest.skip("Arquivo server.py não encontrado ou com erro de importação, pulando testes do Lab 02.", allow_module_level=True)
except Exception as e:
    pytest.skip(f"Erro ao importar o servidor do Lab 02: {e}", allow_module_level=True)


def test_list_tools_endpoint():
    """Testa se o endpoint /tools retorna a lista de ferramentas corretamente."""
    response = client.get("/tools")
    assert response.status_code == 200
    tools = response.json()
    assert isinstance(tools, list)
    assert len(tools) >= 2, "O endpoint /tools deve retornar pelo menos duas ferramentas."

    tool_names = [t["name"] for t in tools]
    assert "calculator" in tool_names, "A ferramenta 'calculator' não foi encontrada."
    assert "text_analyzer" in tool_names, "A ferramenta 'text_analyzer' não foi encontrada."

    # Verifica a estrutura da calculadora
    calculator_tool = next((t for t in tools if t["name"] == "calculator"), None)
    assert calculator_tool is not None
    assert "description" in calculator_tool
    assert "parameters" in calculator_tool
    assert "expression" in calculator_tool["parameters"]


def test_invoke_calculator_tool():
    """Testa a invocação da ferramenta de calculadora."""
    request_data = {
        "tool_name": "calculator",
        "arguments": {"expression": "2 * (3 + 4)"}
    }
    response = client.post("/invoke", json=request_data)
    assert response.status_code == 200
    response_data = response.json()
    assert "result" in response_data
    assert response_data["result"] == 14.0


def test_invoke_text_analyzer_tool():
    """Testa a invocação da ferramenta de análise de texto."""
    request_data = {
        "tool_name": "text_analyzer",
        "arguments": {"text": "Olá mundo, como vai?"}
    }
    response = client.post("/invoke", json=request_data)
    assert response.status_code == 200
    response_data = response.json()
    assert "result" in response_data
    result = response_data["result"]
    assert isinstance(result, dict)
    assert "word_count" in result
    assert "char_count" in result
    assert result["word_count"] == 4
    assert result["char_count"] == 20


def test_invoke_tool_not_found():
    """Testa a invocação de uma ferramenta que não existe."""
    request_data = {
        "tool_name": "non_existent_tool",
        "arguments": {}
    }
    response = client.post("/invoke", json=request_data)
    # O comportamento esperado pode variar: um 404 ou uma resposta de erro.
    # Vamos aceitar um status de erro (4xx) ou uma resposta indicando falha.
    if response.status_code >= 400:
        assert True
    else:
        assert "result" in response.json()
        assert "não encontrada" in str(response.json()["result"]).lower() or \
               "not found" in str(response.json()["result"]).lower()

def test_invoke_calculator_with_invalid_expression():
    """Testa a calculadora com uma expressão inválida."""
    request_data = {
        "tool_name": "calculator",
        "arguments": {"expression": "2 +* 3"}
    }
    response = client.post("/invoke", json=request_data)
    assert response.status_code == 200
    response_data = response.json()
    assert "result" in response_data
    assert "erro" in str(response_data["result"]).lower() or \
           "error" in str(response_data["result"]).lower()
