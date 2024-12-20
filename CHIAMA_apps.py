import streamlit as st
import subprocess

# Funzione per eseguire script.py passando dati come argomenti
def run_external_script(nome_ticker):
    result = subprocess.run(
        ['python', 'subprocess_001.py', nome_ticker],
        capture_output=True,  # Cattura l'output
        text=True  # Gestisci l'output come stringa
    )
    return result.stdout  # Restituisce l'output del subprocess

# Usa la funzione in Streamlit
if st.button('Esegui script'):
    nome_ticker = "AAPL"  # Esempio di ticker
    output = run_external_script(nome_ticker)
    st.write(output)  # Visualizza l'output nell'app Streamlit
