#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:12:56 2024

@author: ninni
"""


import sys
import yfinance as yf

def run_task(nome_ticker):
    print(f"Dati ricevuti dallo script: {nome_ticker}")
    
    #ticker = yf.Ticker(nome_ticker.upper())
    #dati_storici = ticker.history(period="max")
    
    # Aggiungi una gestione del risultato da ritornare
    return f"questo è il valore del subprocess_001 {nome_ticker}"

if __name__ == "__main__":
    nome_ticker = sys.argv[1]  # Recupera l'argomento passato dalla riga di comando
    result = run_task(nome_ticker)
    print(result)  # Stampa il risultato, che sarà catturato dal subprocess.run()
