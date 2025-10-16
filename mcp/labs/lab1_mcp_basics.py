"""
Lab 1: MCP Basics
Introduction to Model Context Protocol server implementation.
"""

from typing import Any, Dict, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class ToolDefinition(BaseModel):
    """MCP Tool definition."""
    name: str
    description: str
    parameters: Dict[str, Any]


class ToolRequest(BaseModel):
    """Tool execution request."""
    name: str
    arguments: Dict[str, Any]


class MCPServer:
    """Basic MCP Server implementation."""
    
    def __init__(self):
        """Initialize MCP server."""
        self.app = FastAPI(title="MCP Lab Server")
        self.tools = {}
        self._setup_routes()
    
    def _setup_routes(self):
        """Setup FastAPI routes."""
        
        @self.app.get("/tools")
        async def list_tools():
            """List available tools."""
            return {
                "tools": [
                    {
                        "name": name,
                        "description": tool["description"],
                        "parameters": tool["parameters"]
                    }
                    for name, tool in self.tools.items()
                ]
            }
        
        @self.app.post("/execute")
        async def execute_tool(request: ToolRequest):
            """Execute a tool."""
            if request.name not in self.tools:
                raise HTTPException(status_code=404, message=f"Tool {request.name} not found")
            
            tool = self.tools[request.name]
            try:
                result = tool["function"](**request.arguments)
                return {"result": result}
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
    
    def exercise_1_register_tool(
        self, 
        name: str, 
        description: str,
        parameters: Dict[str, Any],
        function: callable
    ):
        """
        Exercise 1: Register a new tool with the MCP server.
        
        TODO: Implement this method to:
        1. Store the tool in self.tools dictionary
        2. Key should be the tool name
        3. Value should be a dict with description, parameters, and function
        
        Args:
            name: Tool name
            description: Tool description
            parameters: Parameter schema
            function: The function to execute
        """
        # YOUR CODE HERE
        pass
    
    def exercise_2_calculator_tool(self, operation: str, a: float, b: float) -> float:
        """
        Exercise 2: Implement a calculator tool.
        
        TODO: Implement this method to:
        1. Support operations: add, subtract, multiply, divide
        2. Return the result of the operation
        3. Raise ValueError for unknown operations
        4. Handle division by zero
        
        Args:
            operation: The operation to perform
            a: First number
            b: Second number
            
        Returns:
            Result of the calculation
        """
        # YOUR CODE HERE
        pass
    
    def exercise_3_text_analyzer_tool(self, text: str) -> Dict[str, Any]:
        """
        Exercise 3: Implement a text analyzer tool.
        
        TODO: Implement this method to return:
        1. Character count (including spaces)
        2. Word count
        3. Sentence count (count periods, exclamation marks, question marks)
        4. Average word length
        
        Args:
            text: Text to analyze
            
        Returns:
            Dictionary with analysis results
        """
        # YOUR CODE HERE
        pass


def main():
    """Demo of MCP server lab."""
    server = MCPServer()
    
    # Register calculator tool
    print("Exercise 1 & 2: Register Calculator Tool")
    try:
        server.exercise_1_register_tool(
            name="calculator",
            description="Perform basic math operations",
            parameters={
                "operation": {"type": "string", "enum": ["add", "subtract", "multiply", "divide"]},
                "a": {"type": "number"},
                "b": {"type": "number"}
            },
            function=server.exercise_2_calculator_tool
        )
        print("✓ Calculator tool registered\n")
    except NotImplementedError:
        print("✗ Not implemented yet\n")
    
    print(f"Total tools registered: {len(server.tools)}")


if __name__ == "__main__":
    main()
