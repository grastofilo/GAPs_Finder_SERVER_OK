import streamlit as st
import subprocess

# Funzione per eseguire script.py passando dati come argomenti
def run_external_script(data):
    result = subprocess.run(['python', 'script.py', data], capture_output=True, text=True)
    return result.stdout

# Usa la funzione in Streamlit
if st.button('Esegui script'):
    data = "Dati di esempio"
    output = run_external_script(data)
    st.write(output)
