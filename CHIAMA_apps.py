import streamlit as st
import subprocess
import os

# Funzione per eseguire script.py passando dati tramite variabili d'ambiente
def run_external_script(data):
    # Imposta la variabile d'ambiente
    os.environ['DATA'] = data
    result = subprocess.run(['python', 'script.py'], capture_output=True, text=True)
    return result.stdout

# Usa la funzione in Streamlit
if st.button('Esegui script'):
    data = "Dati di esempio"
    output = run_external_script(data)
    st.write(output)
