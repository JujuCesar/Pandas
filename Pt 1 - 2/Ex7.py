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

print(df)
# Pegando a linha D com loc
linhaD = df.loc['d']
mediaD = linhaD.mean()

# Pegando a linha E com iloc
linhaE = df.iloc[4,:] # Linha E indice 4
somaE = linhaE.sum()

# Saida de dados
print(f"Média da linha D: {mediaD}")
print("")
print(f"Soma da linha E: {somaE}")