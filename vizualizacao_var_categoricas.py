# Utilizando visualizações para variáveis categóricas

# Identificar padroes em uma categoria.

import pandas as pd
import seaborn as sns
from tabulate import tabulate
import matplotlib.pyplot as plt
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#A biblioteca seaborn tem uns dos dataset mais famosos que usam como Iris.

iris = sns.load_dataset("iris")

print(tabulate(iris.head(), headers='keys', tablefmt='fancy_grid', showindex=False))


# Ver as subEspecies da flor iris

print( iris["species"].value_counts)

col = "sepal_length"
sns.histplot(data=iris, x=col, kde=True).set_title(f"Distribuição da variável {col}")

for col in iris.drop(columns = "species"):
    sns.histplot(data=iris, x=col, kde=True).set_title(f"Distribuição da variável {col}")

plt.show() #  Mostrar o gráfico interativamente
plt.close() # Fecha o plot para evitar sobreposição com os próximos plots