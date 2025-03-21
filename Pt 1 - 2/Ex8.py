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

# Pegando linhas A,C, E e colunas X e Y
novo = df.loc[['a','c','e'],['x','y']]
print(f"Linhas A,C, E e colunas X e Y")
print(novo)
print("")

# Somando linhas
somaL = novo.sum(axis=1)

# somando colunas
somaC = novo.sum(axis=0)

# Saida de dados
print(f"Soma das linhas: {somaL}")
print(f"Soma das colunas: {somaC}")