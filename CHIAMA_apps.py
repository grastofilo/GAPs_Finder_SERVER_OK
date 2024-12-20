#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:19:52 2024

@author: ninni
"""

import streamlit as st
import subprocess

# Funzione per eseguire script.py passando dati come argomenti
def run_external_script(nome_ticker):
    result = subprocess.run(['python', 'subprocess_001.py', nome_ticker], capture_output=True, text=True)
    return result.stdout

# Usa la funzione in Streamlit
if st.button('Esegui script'):
    nome_ticker = "SONN"
    output = run_external_script(nome_ticker)
    st.write(output)
