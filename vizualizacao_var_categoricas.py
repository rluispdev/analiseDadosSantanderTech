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

# Iterar sobre as colunas numéricas (excluindo "species")
for col in iris.drop(columns="species"):
    # Gráfico de distribuição (histograma)
    plt.figure(figsize=(12, 5))  # Define o tamanho da figura
    plt.subplot(1, 2, 1)  # Subplot 1: Histograma
    sns.histplot(data=iris, x=col, kde=True, hue="species").set_title(f"Distribuição da variável {col}")

    # Gráfico de barras
    plt.subplot(1, 2, 2)  # Subplot 2: Gráfico de barras
    sns.barplot(data=iris, x="species", hue= iris["species"], y=col, ci=90)
    plt.title(f"Gráfico de barras para {col}")

    plt.tight_layout()  # Ajusta os subplots para não sobrepor elementos
    plt.show()  # Exibe os gráficos