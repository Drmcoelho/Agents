"""
Lab 1: Simple ReAct Agent
Build a basic agent that can reason and take actions.
"""

from typing import Any, Dict, List, Optional


class SimpleTool:
    """A simple tool that an agent can use."""
    
    def __init__(self, name: str, description: str, func: callable):
        self.name = name
        self.description = description
        self.func = func
    
    def run(self, *args, **kwargs) -> Any:
        """Execute the tool."""
        return self.func(*args, **kwargs)


class ReActAgent:
    """
    Simple ReAct (Reasoning + Acting) Agent.
    
    The agent follows the ReAct pattern:
    1. Thought: Reason about what to do
    2. Action: Execute a tool
    3. Observation: See the result
    4. Repeat until done
    """
    
    def __init__(self):
        """Initialize the ReAct agent."""
        self.tools = {}
        self.history = []
        self.max_iterations = 5
    
    def exercise_1_register_tool(self, tool: SimpleTool):
        """
        Exercise 1: Register a tool that the agent can use.
        
        TODO: Implement this method to:
        1. Add the tool to self.tools dictionary
        2. Use tool.name as the key
        3. Store the tool object as the value
        
        Args:
            tool: The tool to register
        """
        # YOUR CODE HERE
        pass
    
    def exercise_2_list_tools(self) -> List[str]:
        """
        Exercise 2: List available tool names.
        
        TODO: Implement this method to:
        1. Return a list of registered tool names
        2. Sort the names alphabetically
        
        Returns:
            List of tool names
        """
        # YOUR CODE HERE
        pass
    
    def exercise_3_get_tool_description(self, tool_name: str) -> Optional[str]:
        """
        Exercise 3: Get the description of a tool.
        
        TODO: Implement this method to:
        1. Look up the tool by name
        2. Return its description
        3. Return None if tool doesn't exist
        
        Args:
            tool_name: Name of the tool
            
        Returns:
            Tool description or None
        """
        # YOUR CODE HERE
        pass
    
    def exercise_4_execute_tool(
        self, 
        tool_name: str, 
        *args, 
        **kwargs
    ) -> Any:
        """
        Exercise 4: Execute a tool and return its result.
        
        TODO: Implement this method to:
        1. Look up the tool by name
        2. Call the tool's run() method with the provided arguments
        3. Store the execution in self.history as a dict with:
           - 'tool': tool name
           - 'args': arguments
           - 'result': the result
        4. Return the result
        5. Raise ValueError if tool doesn't exist
        
        Args:
            tool_name: Name of the tool to execute
            *args: Positional arguments for the tool
            **kwargs: Keyword arguments for the tool
            
        Returns:
            Tool execution result
        """
        # YOUR CODE HERE
        pass
    
    def exercise_5_simple_reasoning(self, task: str) -> str:
        """
        Exercise 5: Simple reasoning loop (hardcoded for demo).
        
        TODO: Implement a simple reasoning loop that:
        1. Prints "Thought: Analyzing task - {task}"
        2. If "calculator" tool exists and task contains "calculate":
           - Execute calculator tool
           - Return the result
        3. Otherwise return "I don't know how to handle this task"
        
        Args:
            task: Task description
            
        Returns:
            Result or message
        """
        # YOUR CODE HERE
        pass


# Example tools for testing
def calculator(operation: str, a: float, b: float) -> float:
    """Simple calculator tool."""
    ops = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else float('inf'),
    }
    return ops[operation](a, b)


def web_search(query: str) -> str:
    """Mock web search tool."""
    return f"Mock search results for: {query}"


def main():
    """Demo of ReAct agent lab."""
    agent = ReActAgent()
    
    # Create tools
    calc_tool = SimpleTool(
        name="calculator",
        description="Perform basic math operations (add, subtract, multiply, divide)",
        func=calculator
    )
    
    search_tool = SimpleTool(
        name="search",
        description="Search the web for information",
        func=web_search
    )
    
    # Test Exercise 1
    print("Exercise 1: Register Tools")
    try:
        agent.exercise_1_register_tool(calc_tool)
        agent.exercise_1_register_tool(search_tool)
        print(f"✓ Registered {len(agent.tools)} tools\n")
    except NotImplementedError:
        print("✗ Not implemented yet\n")
    
    # Test Exercise 2
    print("Exercise 2: List Tools")
    try:
        tools = agent.exercise_2_list_tools()
        print(f"Available tools: {tools}\n")
    except NotImplementedError:
        print("✗ Not implemented yet\n")
    
    # Test Exercise 3
    print("Exercise 3: Get Tool Description")
    try:
        desc = agent.exercise_3_get_tool_description("calculator")
        print(f"Calculator description: {desc}\n")
    except NotImplementedError:
        print("✗ Not implemented yet\n")
    
    # Test Exercise 4
    print("Exercise 4: Execute Tool")
    try:
        result = agent.exercise_4_execute_tool(
            "calculator", 
            operation="add", 
            a=5, 
            b=3
        )
        print(f"5 + 3 = {result}\n")
    except NotImplementedError:
        print("✗ Not implemented yet\n")


if __name__ == "__main__":
    main()
