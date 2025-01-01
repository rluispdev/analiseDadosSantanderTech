#Outliers e tratamento de Outliers - Pontos fora da curva.
import numpy as np
import pandas as pd
from tabulate import tabulate

houses = pd.read_csv('houses_to_rent.csv')

print(tabulate(houses.head(), headers='keys', tablefmt='fancy_grid', showindex=False))

print(tabulate(houses.describe(), headers='keys', tablefmt='fancy_grid', showindex=False))


#Ver a distribuicao dos banheiros nas casas
house_df = houses["bathroom"].value_counts().reset_index()
#converter para usar o tabulate
house_df.columns = ['bathroom', 'count']
print(tabulate(house_df, headers='keys', tablefmt='fancy_grid', showindex=False))

#Criterio de deteteccao de outlieres (pontos fora da curva)

#Criterio IQR -> Distancia inter quartil (Inter quantile range), calcuar uma distancia, mais ou menos do meio da distancia dos dados, cacular
# a distancia entre o registro que esta na posicao 3/4 e o resgistro na posicao 1/4de todos, o primero quartil e 
#terceiro quartil, e vamos dizer que dados que sao maiores que o primeio quartil e mais uma vez e meia essa distancia, 
#sao outliers para mais e dos que forem menores que o primerio quartil menos uma vez e meia essa distancia sao outliers  menores


q1 = houses["bathroom"].quantile(0.25) #primeiro quartil
q3 = houses["bathroom"].quantile(0.75)

IQR = q3 - q1
print(f"IQR: {IQR}")

#Fazer nosso criterio

houses_outliers = houses[(houses["bathroom"] < q1 - ( IQR * 1.5))| (houses["bathroom"] > q3 + ( IQR * 1.5))]
print(tabulate(houses_outliers, headers='keys', tablefmt='fancy_grid', showindex=False))


# Fazer o inliers

house_inliers = houses[(houses["bathroom"] >= q1 - ( IQR * 1.5)) & (houses["bathroom"] <= q3 + ( IQR * 1.5))]
print(tabulate(house_inliers.head(), headers='keys', tablefmt='fancy_grid', showindex=False))

print(tabulate(house_inliers.describe(), headers='keys', tablefmt='fancy_grid', showindex=False))


