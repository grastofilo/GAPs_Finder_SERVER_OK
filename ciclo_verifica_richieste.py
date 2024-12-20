from multiprocessing import Process
from time import sleep
import yfinance as yf
import requests
import streamlit as st


def stress_test(ticker_list, proxy=None, max_iterations=10):
    """Esegue un test sui ticker specificati."""
    cont = 0
    iteration = 0

    while iteration < max_iterations:
        ticker = yf.Ticker(ticker_list[cont])

        # Richiesta 01
        dati_storici = ticker.history(period="max")
        split_01 = dati_storici['Stock Splits'].sum()

        # Richiesta 02 con proxy (se specificato)
        if proxy:
            session = requests.Session()
            session.proxies = {'http': proxy}
            yf._REQUESTS_SESSION = session  # Assegna la sessione personalizzata

        dati_storici_02 = ticker.history(period="max")
        split_02 = dati_storici_02['Stock Splits'].sum()

        st.write(f'Ticker: {ticker_list[cont]} | split_01 = {split_01:.3f} - split_02 = {split_02:.3f}')
        sleep(2)  # Simula una pausa tra le richieste

        # Interrompi il ciclo in caso di discrepanze o condizioni
        if split_01 != split_02:
            st.write("Discrepanza trovata, interruzione del test.")
            break

        # Incrementa il contatore
        cont = (cont + 1) % len(ticker_list)
        iteration += 1
        st.write(cont)


if __name__ == "__main__":
    # Ticker e configurazione
    ticker_round = ['SONN', 'BENF', 'NUKK']
    max_iterations = 20  # Numero massimo di iterazioni
    proxy_1 = 'http://220.248.70.237:9002'  # Proxy opzionale

    # Crea due processi per eseguire il test simultaneamente
    process_1 = Process(target=stress_test, args=(ticker_round, None, max_iterations))
    process_2 = Process(target=stress_test, args=(ticker_round, proxy_1, max_iterations))

    # Avvia i processi
    process_1.start()
    process_2.start()

    # Aspetta la conclusione dei processi
    process_1.join()
    process_2.join()

    st.write("Stress-Test completato.")
