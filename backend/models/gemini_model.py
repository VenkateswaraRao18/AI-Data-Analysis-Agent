import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


class GeminiLLM:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        self.client = genai.Client(api_key=api_key)

        print("Gemini model loaded successfully!")

    def generate(self, prompt):

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text