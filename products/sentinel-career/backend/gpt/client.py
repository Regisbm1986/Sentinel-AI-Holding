from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
model = os.getenv("AZURE_OPENAI_MODEL")

print(f"Endpoint: {endpoint}")
print(f"Model: {model}")

client = OpenAI(
    api_key=api_key,
    base_url=endpoint
)

def ask_gpt(prompt):
    response = client.responses.create(
        model=model,
        input=prompt
    )
    return response.output_text
