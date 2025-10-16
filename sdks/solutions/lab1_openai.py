"""
Lab 1 Solution: OpenAI SDK Basics
"""

import os
from typing import List

from openai import OpenAI


class OpenAILab:
    """OpenAI SDK Lab exercises - SOLUTION."""
    
    def __init__(self):
        """Initialize OpenAI client."""
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment")
        
        self.client = OpenAI(api_key=api_key)
        self.model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    
    def exercise_1_simple_completion(self, prompt: str) -> str:
        """Exercise 1: Create a simple chat completion."""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    
    def exercise_2_system_prompt(self, system: str, user: str) -> str:
        """Exercise 2: Use system prompts to control behavior."""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user}
            ]
        )
        return response.choices[0].message.content
    
    def exercise_3_streaming(self, prompt: str) -> List[str]:
        """Exercise 3: Implement streaming responses."""
        chunks = []
        stream = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )
        
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                chunks.append(chunk.choices[0].delta.content)
        
        return chunks
    
    def exercise_4_temperature_control(
        self, 
        prompt: str, 
        temperature: float = 0.7
    ) -> str:
        """Exercise 4: Control response randomness with temperature."""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )
        return response.choices[0].message.content
