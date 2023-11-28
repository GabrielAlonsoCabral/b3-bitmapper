# SCRIPT IN PROGRESS
import pandas as pd

df = pd.read_csv("_COTAHIST_A2023.csv", low_memory=False)

df1 = df[['CÓDIGO DE NEGOCIAÇÃO DO PAPEL', 'PREÇO DE ABERTURA DO PAPEL-MERCADO NO PREGÃO']]
print(df1.head())
# print(df.head())