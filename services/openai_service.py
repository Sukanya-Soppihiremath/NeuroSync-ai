from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def ask_ai(prompt):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role":"system",
                "content":"""
                You are NeuroSync AI.
                Personal assistant.
                Professional.
                Helpful.
                """
            },
            {
                "role":"user",
                "content":prompt
            }
        ]
    )
    return response.choices[0].message.content