import numpy as np
import pandas as pd

# Lendo o CSV
dfPaises = pd.read_csv('paises.csv', delimiter=';')

# Pegando paises da Oceania
Oceania = dfPaises[dfPaises['Region'].str.contains('OCEANIA')]

# a) Paises da Oceania
paisesOceania = Oceania['Country']

print("Paises da Oceania:")
print(paisesOceania)

print("")
# b) N de paises da Oceania
qtdOceania = len(Oceania)
print(f"Quantidade de paises da Oceania: {qtdOceania}")
