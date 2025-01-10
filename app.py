import streamlit as st
from utils.model_integration import generate_response, validate_and_store

st.title("Chatbot Aprendizado Contínuo")

# Interface do usuário
user_input = st.text_input("Digite sua pergunta:")
if st.button("Enviar"):
    response = generate_response(user_input)
    st.write(f"Resposta: {response}")
    
    # Validação e aprendizado
    feedback = st.radio("A resposta está correta?", ("Sim", "Não"))
    if st.button("Confirmar"):
        result = validate_and_store(user_input, response) if feedback == "Sim" else "Sem alterações."
        st.write(result)
