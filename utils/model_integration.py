from transformers import pipeline
from utils.database import store_information

generator = pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B")

def generate_response(prompt):
    """Gera uma resposta usando Hugging Face GPT-2"""
    response = generator(prompt, max_length=100, num_return_sequences=1)
    return response[0]["generated_text"]

def validate_and_store(prompt, response):
    """Valida e armazena respostas"""
    if "falso" in response.lower():
        return "Informação rejeitada como falsa."
    store_information(prompt, response)
    return "Informação armazenada com sucesso."
