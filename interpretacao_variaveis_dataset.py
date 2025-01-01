import pandas as pd
import seaborn as sns
from tabulate import tabulate
import matplotlib.pyplot as plt

peguins = sns.load_dataset("penguins")
print(tabulate(peguins.head(), headers='keys', tablefmt='fancy_grid', showindex=False))


#Descobrir qual pinguem e baseado em alguma caracteristica

#tipos de pinguins
print(peguins["species"].value_counts())

#Identificar como as variavies inlfuenciam na especie do pinguim, quais variaveis influenciam a massa do pinguin 
#Pra fazer a corretalacao nao podemos deixar strings vamos antes fazer um filtro

pinguins_numeric = peguins.drop(columns=["species", "island", "sex"])
correlation = pinguins_numeric.corr()
print(tabulate(correlation, headers='keys', tablefmt='fancy_grid', showindex=False))

for col in peguins.drop(columns=["species", "island", "sex"]):
    sns.barplot(data=peguins, x="species", y=col, ci=90)
   
   
#Usar um grafico de dispersao para ver a relação entre as variaveis
sns.scatterplot(x="body_mass_g", y="flipper_length_mm", hue="species", data=peguins)

#Mais dispersao
sns.scatterplot(x="body_mass_g", y="bill_length_mm", hue="species", data=peguins)


#Ver todas as combinacoes possiveis
sns.pairplot(peguins, hue="species")

plt.show()  # Exibe os gráficos

