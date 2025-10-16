"""
Lab 1 Solution: Simple ReAct Agent
"""

from typing import Any, List, Optional


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
    """Simple ReAct Agent - SOLUTION."""
    
    def __init__(self):
        """Initialize the ReAct agent."""
        self.tools = {}
        self.history = []
        self.max_iterations = 5
    
    def exercise_1_register_tool(self, tool: SimpleTool):
        """Exercise 1: Register a tool that the agent can use."""
        self.tools[tool.name] = tool
    
    def exercise_2_list_tools(self) -> List[str]:
        """Exercise 2: List available tool names."""
        return sorted(self.tools.keys())
    
    def exercise_3_get_tool_description(self, tool_name: str) -> Optional[str]:
        """Exercise 3: Get the description of a tool."""
        tool = self.tools.get(tool_name)
        return tool.description if tool else None
    
    def exercise_4_execute_tool(
        self, 
        tool_name: str, 
        *args, 
        **kwargs
    ) -> Any:
        """Exercise 4: Execute a tool and return its result."""
        if tool_name not in self.tools:
            raise ValueError(f"Tool '{tool_name}' not found")
        
        tool = self.tools[tool_name]
        result = tool.run(*args, **kwargs)
        
        # Store in history
        self.history.append({
            'tool': tool_name,
            'args': {'args': args, 'kwargs': kwargs},
            'result': result
        })
        
        return result
    
    def exercise_5_simple_reasoning(self, task: str) -> str:
        """Exercise 5: Simple reasoning loop."""
        print(f"Thought: Analyzing task - {task}")
        
        if "calculator" in self.tools and "calculate" in task.lower():
            # Extract operation and numbers (simplified)
            # In reality, you'd use more sophisticated parsing
            result = self.exercise_4_execute_tool(
                "calculator",
                operation="add",
                a=2,
                b=2
            )
            return f"Calculated result: {result}"
        
        return "I don't know how to handle this task"
