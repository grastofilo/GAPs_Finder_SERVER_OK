from time import sleep
import yfinance as yf
import requests
import streamlit as st

# Flag per interrompere il loop
stop = False  # Flag iniziale
if st.button('Stop Stress-Test', key="stop_test"):
    stop = True

cont = 0

while not stop:  # Esegui il loop finché il pulsante non viene premuto
    ticker_round = ['SONN', 'BENF', 'NUKK']
    ticker = yf.Ticker(ticker_round[cont])
    cont += 1

    # Richiesta 01
    dati_storici = ticker.history(period="max")
    split_01 = dati_storici['Stock Splits'].sum()

    # Richiesta 02 con proxy
    proxies = {'http': 'http://220.248.70.237:9002'}
    session = requests.Session()
    session.proxies = proxies
    yf._REQUESTS_SESSION = session  # Assegna la sessione personalizzata

    dati_storici_02 = ticker.history(period="max")
    split_02 = dati_storici_02['Stock Splits'].sum()

    st.write(f'split_01 = {split_01:.3f} - split_02 = {split_02:.3f}')
    sleep(2)

    # Interrompi il loop se ci sono discrepanze o condizioni particolari
    if split_01 != split_02:
        break
    if cont == 0 and (split_01 < 2.90 or split_02 < 2.90):
        break
    if cont == 3:
        cont = 0

    # Verifica nuovamente il flag di interruzione
    if st.button('Stop Stress-Test', key="stop_loop"):
        stop = True

st.write("Stress-Test terminato.")
