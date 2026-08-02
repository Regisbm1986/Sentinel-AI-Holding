from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_ENDPOINT")
)

response = client.responses.create(
    model=os.getenv("AZURE_OPENAI_MODEL"),
    input="Responda apenas: MODELO_OK_GPT41"
)

print(response.output_text)
