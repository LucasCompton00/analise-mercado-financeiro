import pandas as pd
import requests

url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.4390/dados?formato=json&dataInicial=01/01/2025&dataFinal=31/12/2025"

resposta = requests.get(url, timeout=20)
resposta.raise_for_status()
dados = resposta.json()
df = pd.DataFrame(dados)  

df["valor"] = pd.to_numeric(df["valor"])
df["data"] = pd.to_datetime(df["data"], format = "%d/%m/%Y") 

df = df.rename(columns={"data": "data_referencia", "valor": "taxa_percentual"})

print(df)
print(df.dtypes)

df.to_csv("selic_2025.csv", index=False)