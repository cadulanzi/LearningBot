import chromadb
from chromadb.config import Settings

# Configuração do cliente ChromaDB
client = chromadb.Client(Settings(persist_directory="./db_storage"))

def store_information(key, value):
    """Armazena informações relevantes no banco de dados vetorial"""
    collection = client.get_or_create_collection(name="chatbot_data")
    collection.add(documents=[value], metadatas=[{"prompt": key}], ids=[key])

def query_information(key):
    """Consulta informações armazenadas no banco de dados vetorial"""
    collection = client.get_collection(name="chatbot_data")
    results = collection.query(query_texts=[key], n_results=1)
    return results
