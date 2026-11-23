import pandas as pd
dados = {
    "mes": ["Janeiro", "Fevereiro", "Março"],
    "selic": [1.01, 0.99, 0.96]
}

df = pd.DataFrame(dados)

print(round(df["selic"].mean(), 2))

print(df["selic"].max())

print(df["selic"].idxmax())

print(df.loc[df["selic"].idxmax(), "mes"])

print(df.loc[df["selic"].idxmin(), "mes"])