"""
Lab 1: OpenAI SDK Basics
Learn how to use the OpenAI SDK for text generation and chat completions.
"""

import os
from typing import List, Optional

from openai import OpenAI


class OpenAILab:
    """OpenAI SDK Lab exercises."""
    
    def __init__(self):
        """Initialize OpenAI client."""
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment")
        
        self.client = OpenAI(api_key=api_key)
        self.model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    
    def exercise_1_simple_completion(self, prompt: str) -> str:
        """
        Exercise 1: Create a simple chat completion.
        
        TODO: Implement this method to:
        1. Create a chat completion using self.client.chat.completions.create()
        2. Use self.model as the model parameter
        3. Pass the prompt as a user message
        4. Return the assistant's response text
        
        Args:
            prompt: The user's input prompt
            
        Returns:
            The assistant's response text
        """
        # YOUR CODE HERE
        pass
    
    def exercise_2_system_prompt(self, system: str, user: str) -> str:
        """
        Exercise 2: Use system prompts to control behavior.
        
        TODO: Implement this method to:
        1. Create a chat completion with both system and user messages
        2. System message should set the assistant's behavior
        3. Return the assistant's response
        
        Args:
            system: The system prompt
            user: The user's message
            
        Returns:
            The assistant's response text
        """
        # YOUR CODE HERE
        pass
    
    def exercise_3_streaming(self, prompt: str) -> List[str]:
        """
        Exercise 3: Implement streaming responses.
        
        TODO: Implement this method to:
        1. Create a streaming chat completion (stream=True)
        2. Collect all chunks into a list
        3. Return the list of text chunks
        
        Args:
            prompt: The user's input prompt
            
        Returns:
            List of response chunks
        """
        # YOUR CODE HERE
        pass
    
    def exercise_4_temperature_control(
        self, 
        prompt: str, 
        temperature: float = 0.7
    ) -> str:
        """
        Exercise 4: Control response randomness with temperature.
        
        TODO: Implement this method to:
        1. Create a chat completion with custom temperature
        2. Temperature should be between 0.0 and 2.0
        3. Return the response
        
        Args:
            prompt: The user's input prompt
            temperature: Sampling temperature (0.0 to 2.0)
            
        Returns:
            The assistant's response text
        """
        # YOUR CODE HERE
        pass


def main():
    """Demo of OpenAI SDK lab."""
    lab = OpenAILab()
    
    # Test exercise 1
    print("Exercise 1: Simple Completion")
    try:
        response = lab.exercise_1_simple_completion("What is AI?")
        print(f"Response: {response}\n")
    except NotImplementedError:
        print("Not implemented yet\n")
    
    # Test exercise 2
    print("Exercise 2: System Prompt")
    try:
        response = lab.exercise_2_system_prompt(
            system="You are a helpful tutor who explains concepts simply.",
            user="What is machine learning?"
        )
        print(f"Response: {response}\n")
    except NotImplementedError:
        print("Not implemented yet\n")


if __name__ == "__main__":
    main()
