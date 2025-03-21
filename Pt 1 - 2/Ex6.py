import numpy as np
import pandas as pd

# DataFrames

# Criando semente de random
np.random.seed(10)

# Criando o dataframe
df = pd.DataFrame(index=['a','b','c','d','e'],
                  columns=['w','x','y','z'],
                  data=np.random.randint(1,50,[5,4])
                  )

# Filtrando a coluna x menores que 30
filtro = df ['x'][df ['x'] >= 30]

# Fazendo a media do trem
media = filtro.mean()

# Saida de dados
print(f"Média dos valores: {media}")

