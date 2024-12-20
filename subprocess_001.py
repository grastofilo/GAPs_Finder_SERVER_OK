#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:12:56 2024

@author: ninni
"""

import sys

def run_task(nome_ticker):
    
    print(f"Dati ricevuti dallo script: {nome_ticker}")
    return f"Risultato: il tuo ticker è {nome_ticker}"

if __name__ == "__main__":
    nome_ticker = sys.argv[1]  # Recupera l'argomento passato dalla riga di comando
    print(run_task(nome_ticker))
