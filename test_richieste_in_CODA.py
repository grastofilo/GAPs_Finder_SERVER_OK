import yfinance as yf
import streamlit as st
import time
from queue import Queue
from threading import Thread

# Funzione per processare le richieste in coda
def process_queue(queue, result_queue):
    while True:
        ticker_symbol = queue.get()  # Ottieni il lavoro dalla coda
        if ticker_symbol is None:  # Condizione per terminare il thread
            break
        
        # Esegui la richiesta a YFinance
        ticker = yf.Ticker(ticker_symbol)
        dati_storici = ticker.history(period="max")
        split_sum = dati_storici['Stock Splits'].sum()
        
        # Metti il risultato nella coda dei risultati
        result_queue.put((ticker_symbol, split_sum))
        time.sleep(2)  # Ritardo tra le richieste per evitare rate limiting
        queue.task_done()

# Creazione delle code
task_queue = Queue()
result_queue = Queue()

# Avvia un thread per processare la coda
thread = Thread(target=process_queue, args=(task_queue, result_queue))
thread.daemon = True
thread.start()

# Interfaccia Streamlit
st.title("Stress-Test con YFinance")
tickers = st.text_input("Inserisci i ticker separati da una virgola (es. SONN,BENF,NUKK):")

if st.button("Avvia Test"):
    ticker_list = [ticker.strip() for ticker in tickers.split(",")]
    
    # Aggiungi i ticker alla coda
    for ticker in ticker_list:
        task_queue.put(ticker)
    
    st.write("Esecuzione in corso...")
    
    # Mostra i risultati man mano che vengono processati
    while not task_queue.empty() or not result_queue.empty():
        if not result_queue.empty():
            ticker_symbol, split_sum = result_queue.get()
            st.write(f"Ticker: {ticker_symbol}, Stock Splits: {split_sum:.3f}")
        time.sleep(0.1)

    # Pulizia finale
    task_queue.put(None)  # Segnale per terminare il thread
    thread.join()
