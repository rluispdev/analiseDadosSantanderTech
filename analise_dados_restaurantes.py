import numpy as np
import pandas as pd
from tabulate import tabulate

cuisine_rating = pd.read_csv('cuisine_rating.csv')

#print(tabulate( cuisine_rating, headers='keys', tablefmt='fancy_grid', showindex=False))

#Fazer um somatizacao  com a func describe() e temos uns dados de count, meab, std, min, 25%, 50%, 75%, max

print(tabulate( cuisine_rating.describe(), headers='keys', tablefmt='fancy_grid', showindex=False))

#verificar quais regioes disponiveis

# Converter locations para um DF antes de passar para o tabulate
locations = cuisine_rating["Location"].value_counts().reset_index()
locations.columns = ['Location', 'Count']
print(tabulate(locations, headers='keys', tablefmt='fancy_grid', showindex=False))


#Descobir no Central Parque a culinaria mais avaliada, calcular a media e a mediana das avalaicoes 
#agrupando pela regiao.

#filtras somente das columas numericas

numerics_cols = cuisine_rating.select_dtypes(include=[np.number]).columns.tolist()
print(numerics_cols)

locations = cuisine_rating.groupby("Location")[numerics_cols].mean()
print(tabulate(locations, headers='keys', tablefmt='fancy_grid', showindex=False))

#passar tambem a culinaria

locations = cuisine_rating.groupby(["Location", "Cuisines"])[numerics_cols].mean()
print(tabulate(locations, headers='keys', tablefmt='fancy_grid', showindex=False))