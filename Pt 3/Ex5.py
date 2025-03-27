import numpy as np
import pandas as pd

# Lendo o CSV
dfPaises = pd.read_csv('paises.csv', delimiter=';')

# Criando função
def classificarMortalidade(deathrate):
    return 'Balanced' if deathrate < 9 else 'Urgent'

# Aplicando a função e criando a nova coluna
dfPaises['Humanitarian Help'] = dfPaises['Deathrate'].apply(classificarMortalidade)

# Saida de dados
print(dfPaises)

