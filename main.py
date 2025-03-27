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
#np.random.seed(10)

# Criando o dataframe
#df = pd.DataFrame(index=['a','b','c','d','e'],
                  #columns=['w','x','y','z'],
                  #data=np.random.randint(1,50,[5,4])
                  #)

#print(df)

#print("")
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
#print(df.loc[['a','b'],['w','x','y','z']])

#print("")
# Slicing com o iloc()
#print(df.iloc[0:2,:])


#----------//-------------------//-------------------//-------------------//-------------------//----------


# Lendo o arquivo csv de paises
#dfPaises = pd.read_csv('paises_V2.csv', delimiter=';')

#print(dfPaises)

# Acessando com facilidade as colunas do DataFrame - Facilita o Slicing
#print(dfPaises.columns)

# Acessando com facilidade os primeiros elementos do DataFrame
#print(dfPaises.head(3))

# Acessando com facilidade os ultimos elementos do DataFrame
#print(dfPaises.tail(3))

# Pegando a % que a pop de um pais representa no mundo
# Calculando a população mundial
#totalPop = np.sum(dfPaises['Population'])

# Fazendo o broadcasting para calcular
#seriesPaisPop = (dfPaises['Population']/totalPop)*100

# Adicionando uma nova coluna no csv
#dfPaises['%Population'] = np.round(seriesPaisPop, 3)

# Gerando um novo arquivo com essa coluna :D
#dfPaises.to_csv('paises_V2.csv', sep=';')

# Pegando os 6 paises mais populosos do planeta
#print(dfPaises.nLargest(6, '%Population'))

# ------------ // ------------- // -------------- // --------------- // --------------

# Agrupamento de Dados

# Agrupando paises por regiao e contando
#groupRegion = dfPaises.groupby('Region')
#print(groupRegion.count()['Country'])

# Soma da pop de cada regiao
#print(groupRegion.sum()['Population'])

# Criando metodo python
#def tenpercent(x):
  #return x*0.9

# Aplicando a função customizada em uma series
#taxaMortalidade = dfPaises['Deathrate']

#taxaMortalidade2 = taxaMortalidade.apply(tenpercent)

# Juntando duas series
#print(pd.concat([taxaMortalidade, taxaMortalidade2], axis=1))