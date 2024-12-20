#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:12:56 2024

@author: ninni
"""

import sys

def run_task(nome_ticker):
    
    ticker = yf.Ticker(nome_ticker.upper())
    dati_storici =  ticker.history(period="max")
    
    return f'questo è il valore del subprocess_001 dati_storici['Stock Splits'].sum()'
    
if __name__ == "__main__":
    nome_ticker = sys.argv[1]  # Recupera l'argomento passato dalla riga di comando
    print(run_task(nome_ticker))
