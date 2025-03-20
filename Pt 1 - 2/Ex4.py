import numpy as np
import pandas as pd

# Criando Series doas Ano 1 e 2
seriesAno1 = pd.Series({'Java':16.25,'C': 16.04,'Python':9.85})
seriesAno2 = pd.Series({'C':16.21,'Python':12.12,'Java':11.68})

# Calculando a variação
variacao = seriesAno2 - seriesAno1

# Pegando positivos
crescimento = variacao[variacao > 0]

# Saida de dados
print("Crescimentos:")
print("")
print(crescimento)
