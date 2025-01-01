# Dado Constanto e dado erronio

import numpy as np
import pandas as pd
from tabulate import tabulate

houses_sp = pd.read_csv('houses_sp.csv')

#verificar as 10 primeiras linhas do DF.

print(tabulate(houses_sp.head(10), headers='keys', tablefmt='fancy_grid', showindex=False))

#Verificar quais cidedades temos para alugar

print(houses_sp["city"].value_counts())

#Verificamos que a culuna da cidade é somente SP, ela entao é constante sendo assim podemso remover essa coluna.

houses_sp = houses_sp.drop(columns=["city"])
print(tabulate(houses_sp.head(10), headers='keys', tablefmt='fancy_grid', showindex=False))

#Dados Erroneos - Com dados dos rooms null (nan) vamos calcular a mediana para nao perdermos esses dados

print(houses_sp["rooms"].median())

#Como usar a mediana de 3 quartos por casa para preencher os dados nulos na caluna rooms.

houses_sp["rooms"] = houses_sp["rooms"].fillna(houses_sp["rooms"].median())

print(tabulate(houses_sp.head(10), headers='keys', tablefmt='fancy_grid', showindex=False))

#Dados digtados errados. Verifacamos na tabela o erro: -

#Filtrando para vermos quantos erros desse tipo temos

print(houses_sp["floor"].value_counts()) # temos 1847 - seria uma perda muito ruim.

#Iriamos validar com a area de negocio  que a casa estaria no andar 0. E fariamos a substituicao.

houses_sp.loc[houses_sp["floor"] == "-", "floor"] = "0"

print(tabulate(houses_sp.head(), headers='keys', tablefmt='fancy_grid', showindex=False))