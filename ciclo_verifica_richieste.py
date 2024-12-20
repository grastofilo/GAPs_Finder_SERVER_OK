from multiprocessing import Process
import time
import yfinance as yf
import requests

def fetch_data(process_id, iterations):
    """
    Funzione che esegue il fetch dei dati per un certo numero di iterazioni.
    process_id: ID del processo, usato per identificare il processo attivo.
    iterations: Numero di cicli che ogni processo esegue.
    """
    ticker_round = ['SONN', 'BENF', 'NUKK']  # Lista di ticker
    proxies = {'http': 'http://220.248.70.237:9002'}  # Proxy da usare (modifica se necessario)

    session = requests.Session()
    session.proxies = proxies  # Configura il proxy per la sessione

    for i in range(iterations):  # Numero totale di iterazioni (modifica qui per allungare il ciclo)
        ticker_symbol = ticker_round[i % len(ticker_round)]  # Ciclo sui ticker
        ticker = yf.Ticker(ticker_symbol, session=session)

        # Prima richiesta
        dati_storici_01 = ticker.history(period="max")
        split_01 = dati_storici_01['Stock Splits'].sum()

        # Seconda richiesta con proxy
        dati_storici_02 = ticker.history(period="max")
        split_02 = dati_storici_02['Stock Splits'].sum()

        st.write(f"Process {process_id}: Iteration {i+1}/{iterations} - Ticker: {ticker_symbol}")
        st.write(f"split_01 = {split_01:.3f}, split_02 = {split_02:.3f}")

        # Simula una pausa per evitare richieste troppo veloci
        time.sleep(2)

def run_processes():
    """
    Avvia due processi paralleli per simulare lo stress-test.
    """
    process_count = 2  # Numero di processi (modifica per aggiungere più processi)
    iterations_per_process = 100  # Numero di cicli per processo (modifica qui per allungare il ciclo)

    processes = []
    for process_id in range(process_count):
        process = Process(target=fetch_data, args=(process_id, iterations_per_process))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

if __name__ == "__main__":
    run_processes()


