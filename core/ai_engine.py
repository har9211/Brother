import os

from dotenv import load_dotenv
from groq import Groq


# Load environment variables from .env
load_dotenv()


class AIEngine:
    """
    Core AI Engine.

    Handles communication between Brother and the AI model.
    """

    def __init__(self, model: str = "llama-3.3-70b-versatile"):
        self.model = model

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError(
                "GROQ_API_KEY not found. Please check your .env file."
            )

        self.client = Groq(api_key=api_key)

    def ask(self, prompt: str) -> str:
        """
        Send a prompt to the AI model and return its response.
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.choices[0].message.content