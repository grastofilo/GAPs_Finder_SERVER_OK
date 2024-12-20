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
        try:
            dati_storici = ticker.history(period="max")
            split_sum = dati_storici['Stock Splits'].sum()
        except Exception as e:
            split_sum = None
            result_queue.put((ticker_symbol, split_sum, str(e)))
        else:
            # Metti il risultato nella coda dei risultati
            result_queue.put((ticker_symbol, split_sum, None))
        
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
    
    # Genera 100 richieste, replicando i ticker
    ticker_requests = ticker_list * 10  # 10 volte per ottenere 100 richieste
    
    # Aggiungi i ticker alla coda
    for ticker in ticker_requests:
        task_queue.put(ticker)
    
    st.write("Esecuzione in corso...")
    
    start_time = time.time()  # Inizia a contare il tempo
    elapsed_time = 0
    timeout = 60  # Timeout in secondi per il blocco del processo

    while True:
        # Controlla se ci sono risultati da mostrare
        try:
            ticker_symbol, split_sum, error = result_queue.get(timeout=5)  # Timeout per evitare blocchi
            if error:
                st.write(f"Errore con il ticker {ticker_symbol}: {error}")
            else:
                st.write(f"Ticker: {ticker_symbol}, Stock Splits: {split_sum:.3f}")
            result_queue.task_done()
        except:
            # Se non ci sono risultati, esci dal loop
            if task_queue.empty() and result_queue.empty():
                break
            elapsed_time = time.time() - start_time
            if elapsed_time > timeout:
                st.write("Il proc
