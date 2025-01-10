from langchain import OpenAI
from langchain.chains import ConversationChain
from utils.database import store_information

def get_llm():
    """Inicializa o modelo de linguagem"""
    return ConversationChain(llm=OpenAI(temperature=0.5))

def generate_response(prompt):
    """Gera uma resposta a partir de um prompt"""
    llm = get_llm()
    return llm.run(prompt)

def validate_and_store(prompt, response):
    """Valida e armazena respostas com base em regras"""
    if "falso" in response.lower():
        return "Informação rejeitada como falsa."
    store_information(prompt, response)
    return "Informação armazenada com sucesso."
