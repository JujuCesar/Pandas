import numpy as np
import pandas as pd

# Lendo o CSV
dfPaises = pd.read_csv('paises.csv', delimiter=';')

# Pegando paises sem costa maritima
paisesSemCosta = dfPaises[dfPaises['Coastline (coast/area ratio)'] == 0]['Country']

# Salvando no arquivo noCoast.csv
paisesSemCosta.to_csv('noCoast.csv', sep=';')