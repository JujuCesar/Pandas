import numpy as np
import pandas as pd

# Criando series com um dicionario
#s2 = pd.Series({'a':10,'c':50, 'd':80})

# Criando Series doas Ano 1 e 2
seriesAno1 = pd.Series({'Java':16.25,'C': 16.04,'Python':9.85})
seriesAno2 = pd.Series({'C':16.21,'Python':12.12,'Java':11.68})

# Retornando porcentagem total que elas representam
total1 = seriesAno1.sum()
total2 = seriesAno2.sum()

# Saida de dados
print(f"Porcentagem total do ano 1: {total1:.2f}%")
print("")
print(f"Porcentagem total do ano2 : {total2:.2f}%")