import numpy as np
import pandas as pd
from tabulate import tabulate

cuisine_rating = pd.read_csv('cuisine_rating.csv')

mostra_cinco_primerias_linhas = cuisine_rating.head()

print(tabulate(mostra_cinco_primerias_linhas, headers='keys', tablefmt='fancy_grid', showindex=False))

print(cuisine_rating.info())

#Filtrar um tipo de cukinaria especifica, e com value_counts contar quantas vezes ela aparece.

print(cuisine_rating["Cuisines"].value_counts())

#Olhar apenas nas avliacoes japonesas

japnese = cuisine_rating[cuisine_rating["Cuisines"] == "Japanese"]
print(tabulate(japnese, headers='keys', tablefmt='fancy_grid', showindex=False))

#Filtrar a media
media_cuisine_japonese = japnese = cuisine_rating[cuisine_rating["Cuisines"] == "Japanese"]["Overall Rating"].mean()
print(media_cuisine_japonese)

