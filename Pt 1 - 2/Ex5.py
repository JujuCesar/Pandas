import numpy as np
import pandas as pd

# Criando Series doas Ano 1 e 2
seriesAno1 = pd.Series({'Java':16.25,'C': 16.04,'Python':9.85})
seriesAno2 = pd.Series({'C':16.21,'Python':12.12,'Java':11.68})

# Calculando a variação
variacao = seriesAno2 - seriesAno1

# Calculando a projeção para dois anos
proj = seriesAno2 + 2 * variacao

# Pegando a linguagem mais popular
pop = proj.nlargest(1)

# Saida de dados
print("Projeção das linguagens: ")
print(proj)
print("")
print("Linguagem mais popular: ")
print(pop)