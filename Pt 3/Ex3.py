import numpy as np
import pandas as pd

# Lendo o CSV
dfPaises = pd.read_csv('paises.csv', delimiter=';')

# Agrupando por Região e calculando a média de alfabetização
mediaAlfabetizacao = dfPaises.groupby('Region')['Literacy (%)'].mean()

# Saida de dados
print(mediaAlfabetizacao)