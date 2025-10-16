"""
B2C Customer Service Agent - Capstone Project
An intelligent customer service chatbot with ChatKit UI.
"""

import os
from typing import Dict, List, Optional

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from rich.console import Console

console = Console()


class B2CAgent:
    """B2C Customer Service Agent."""
    
    def __init__(self):
        """Initialize the B2C agent."""
        self.conversation_history = {}
        
        # Knowledge base (simplified for demo)
        self.knowledge_base = {
            "returns": "You can return items within 30 days of purchase.",
            "shipping": "We offer free shipping on orders over $50.",
            "payment": "We accept credit cards, PayPal, and digital wallets.",
            "hours": "Our customer service is available 24/7.",
        }
    
    def process_message(
        self, 
        message: str, 
        customer_id: str,
        context: Optional[Dict] = None
    ) -> Dict:
        """
        Process a customer message and generate a response.
        
        TODO: Implement full agent logic with:
        - Intent classification
        - RAG-based knowledge retrieval
        - Multi-turn conversation handling
        - Sentiment analysis
        - Escalation logic
        
        Args:
            message: Customer's message
            customer_id: Unique customer identifier
            context: Additional context
            
        Returns:
            Response dictionary with message and metadata
        """
        console.print(f"[blue]Customer {customer_id}:[/blue] {message}")
        
        # TODO: Implement intent classification
        intent = self._classify_intent(message)
        
        # TODO: Implement RAG retrieval
        # TODO: Implement response generation
        # TODO: Implement sentiment analysis
        # TODO: Check escalation conditions
        
        response = {
            "message": "I'm here to help! This is a demo response.",
            "intent": intent,
            "confidence": 0.8,
            "should_escalate": False,
        }
        
        # Store in conversation history
        if customer_id not in self.conversation_history:
            self.conversation_history[customer_id] = []
        
        self.conversation_history[customer_id].append({
            "customer": message,
            "agent": response["message"],
        })
        
        return response
    
    def _classify_intent(self, message: str) -> str:
        """
        Classify customer intent.
        
        TODO: Implement proper intent classification
        """
        message_lower = message.lower()
        
        if "return" in message_lower:
            return "returns"
        elif "ship" in message_lower:
            return "shipping"
        elif "pay" in message_lower:
            return "payment"
        else:
            return "general"
    
    def get_conversation_history(self, customer_id: str) -> List[Dict]:
        """Get conversation history for a customer."""
        return self.conversation_history.get(customer_id, [])


# Flask application
app = Flask(__name__)
CORS(app)

agent = B2CAgent()


@app.route('/')
def index():
    """Serve the chat interface."""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>B2C Customer Service</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
            }
            .chat-container {
                border: 1px solid #ddd;
                border-radius: 10px;
                padding: 20px;
                height: 400px;
                overflow-y: auto;
                margin-bottom: 20px;
            }
            .message {
                margin: 10px 0;
                padding: 10px;
                border-radius: 5px;
            }
            .customer {
                background-color: #e3f2fd;
                text-align: right;
            }
            .agent {
                background-color: #f5f5f5;
            }
            .input-container {
                display: flex;
                gap: 10px;
            }
            input {
                flex: 1;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
            button {
                padding: 10px 20px;
                background-color: #2196F3;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background-color: #1976D2;
            }
        </style>
    </head>
    <body>
        <h1>💬 B2C Customer Service</h1>
        <div class="chat-container" id="chat"></div>
        <div class="input-container">
            <input type="text" id="message" placeholder="Type your message...">
            <button onclick="sendMessage()">Send</button>
        </div>
        
        <script>
            const customerId = 'customer_' + Math.random().toString(36).substr(2, 9);
            
            function addMessage(text, isCustomer) {
                const chat = document.getElementById('chat');
                const msg = document.createElement('div');
                msg.className = 'message ' + (isCustomer ? 'customer' : 'agent');
                msg.textContent = text;
                chat.appendChild(msg);
                chat.scrollTop = chat.scrollHeight;
            }
            
            async function sendMessage() {
                const input = document.getElementById('message');
                const message = input.value.trim();
                
                if (!message) return;
                
                addMessage(message, true);
                input.value = '';
                
                try {
                    const response = await fetch('/chat', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({
                            message: message,
                            customer_id: customerId
                        })
                    });
                    
                    const data = await response.json();
                    addMessage(data.message, false);
                } catch (error) {
                    addMessage('Sorry, there was an error. Please try again.', false);
                }
            }
            
            document.getElementById('message').addEventListener('keypress', (e) => {
                if (e.key === 'Enter') sendMessage();
            });
            
            // Welcome message
            addMessage('Hello! How can I help you today?', false);
        </script>
    </body>
    </html>
    """


@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages."""
    data = request.json
    message = data.get('message')
    customer_id = data.get('customer_id', 'anonymous')
    
    response = agent.process_message(message, customer_id)
    
    return jsonify(response)


def main():
    """Main application entry point."""
    console.print("\n[bold blue]💬 B2C Customer Service Agent[/bold blue]\n")
    
    port = int(os.getenv('B2C_SERVICE_PORT', 3000))
    
    console.print(f"[green]Starting server on http://localhost:{port}[/green]")
    console.print("[dim]Open the URL in your browser to chat with the agent[/dim]\n")
    
    app.run(host='0.0.0.0', port=port, debug=True)


if __name__ == "__main__":
    main()
