from time import sleep


cont = 0
while 0 < 1:
    
    ticker_round = ['SONN','BENF','NUKK']
    
    
    
    ticker = yf.Ticker(ticker_round[cont])
    cont +=1
    
    # richiesta 01
    dati_storici = ticker.history(period="max")
    split_01 = dati_storici['Stock Splits'].sum()
     
    
    
    # richiesta 02
    
    proxies = {'http': 'http://220.248.70.237:9002'}

    # Creazione di una sessione custom con il proxy
    session = requests.Session()
    session.proxies = proxies

    # Usa la sessione per fare la richiesta a yfinance
    yf._REQUESTS_SESSION = session  # Assegna la sessione personalizzata
  
    dati_storici_02 =  ticker.history(period="max")  # dati periodo massimo disponibile  
    split_02 = dati_storici_02['Stock Splits'].sum()



    

    print(f'split_01 = {split_01: .3f} - split_02 = {split_02: .3f}')
    sleep(2)
    
    if split_01 != split_02:
        break
    


    if cont == 0 and (split_01<2.90 or split_02 <2.90):
        break



    if cont == 3:
        cont = 0


    st.button("stop"):
        break
