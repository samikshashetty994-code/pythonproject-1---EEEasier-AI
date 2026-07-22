from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")
key = os.getenv("OPENROUTER_API_KEY")

print("STREAMLIT KEY:", key[:10] if key else "NO KEY")



key = os.getenv("OPENROUTER_API_KEY")

print("Key loaded:", key[:10])


client = OpenAI(
    api_key=key,
    base_url="https://openrouter.ai/api/v1"
)


def ask_ai(question):

    response = client.chat.completions.create(
        model="deepseek/deepseek-r1",

        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content