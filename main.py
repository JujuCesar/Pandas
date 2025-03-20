#Pandas
# - Series -> (1D - Vetor)
# - DataFrame -> (2 ou mais D - Matrizes)

#Criando Series
# - Precisa-se passar duas coisas, as Labels e os dados, como um dicionário

#Criando DataFrames
# - Precisa-se passar três coisas, as index(x), columns(y) e os dados

#----------//-------------------//-------------------//-------------------//-------------------//----------

import numpy as np
import pandas as pd

#labels = ['a', 'b', 'c']
#dados = [10,20,30]

# Criando series com duas listas
#s1 = pd.Series(index = labels, data= dados)

# Criando series com um dicionario
#s2 = pd.Series({'a':10,'c':50, 'd':80})

#print(s1)
#print(type(s1))

# Chamando um valor da Seires
#print(s1['b'])

# Operações entre as series
#print(s1 + s2)
#print("")
#print(s1.add(s2, fill_value=0))

# Acessar apenas o que precisamos
#print(s1[['a','c']])

# Condicionais no Pandas (Identico ao Numpy)
#print(s1 > s1.mean())
#print(s1[s1 > s1.mean()])

# DataFrames

# Criando semente de random
np.random.seed(10)

# Criando o dataframe
df = pd.DataFrame(index=['a','b','c','d','e'],
                  columns=['w','x','y','z'],
                  data=np.random.randint(1,50,[5,4])
                  )

print(df)

print("")
# Slicing das colunas W e Z
#print(df[['w','z']])

#print("")
# Slicing das linhas a e c
#print(df.loc[['a','c']])

#print("")
# Acessar um elemento especifico
#print(df['x']['b'])

# Fazendo slicing com loc() ou iloc()

# Slicing das linhas a e c com loc
print(df.loc[['a','b'],['w','x','y','z']])

print("")
# Slicing com o iloc()
print(df.iloc[0:2,:])



