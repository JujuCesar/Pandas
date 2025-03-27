import numpy as np
import pandas as pd

# Lendo o CSV
dfPaises = pd.read_csv('paises.csv', delimiter=';')

# Encontrar o país com a maior população
paisMaiorPop = dfPaises.loc[dfPaises['Population'].idxmax(), ['Country', 'Region', 'Population']]

# Econtrando o pais mais populoso
maiorPop = dfPaises.nlargest(1, 'Population')[['Country','Region']]

# Saida de dados
print(maiorPop)