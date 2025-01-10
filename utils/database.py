from chromadb import Client
from chromadb.config import Settings

def get_chroma_client():
    """Configura o cliente ChromaDB"""
    return Client(Settings(persist_directory="./db_storage", chroma_type="local"))

def store_information(key, value):
    """Armazena informações relevantes"""
    client = get_chroma_client()
    client.insert(key, value)

def query_information(key):
    """Consulta informações armazenadas"""
    client = get_chroma_client()
    return client.query(key)
