import os

def run_task():
    data = os.getenv('DATA')  # Ottieni il valore della variabile d'ambiente
    print(f"Dati ricevuti dallo script: {data}")
    return f"Risultato: {data}"

if __name__ == "__main__":
    print(run_task())
