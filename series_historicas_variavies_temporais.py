import pandas as pd
import seaborn as sns
from tabulate import tabulate
import matplotlib.pyplot as plt


candy = pd.read_csv("candy_production.csv")
print(tabulate(candy.head(12), headers='keys', tablefmt='fancy_grid', showindex=False))


#Sazionalidade

#Verificar os dados
print(candy.info())

# Percebemos que a data esta sendo interpretada como object, vamos converter para datetime

candy["observation_date"] = pd.to_datetime(candy["observation_date"])
print(candy.info())


#Conseguimos vizualizar nosso grafico , todos anos

candy.plot(x= "observation_date", y="industrial_production")
 
# Fazer um recorte, fazer recorete apartir de 2010.

candy_filtered = candy[candy["observation_date"] >= "2010-01-01"]

#Organizar no exio para melhor vizualização
ax = candy_filtered.plot(x= "observation_date", y="industrial_production", figsize=(12,6))

#Adicionar algumas linhas para demarcar o eixo vertical.
ax = candy_filtered.plot(x= "observation_date", y="industrial_production", figsize=(12,6))
xcoords = ['2010-01-01', '2011-01-01', '2012-01-01', '2013-01-01', '2014-01-01', '2015-01-01', '2016-01-01', '2017-01-01']

for xc in xcoords:
    plt.axvline(x=xc, color='green', linestyle='--')


#Usar modelagem estastica: decomposicao da sazionalidade
from statsmodels.tsa.seasonal import seasonal_decompose # type: ignore

#fazer a conversao do observation_time para que ele seja o indice , porque a func vai pedir isso 
candy_filtered.set_index("observation_date", inplace=True)

analysis = candy_filtered[["industrial_production"]].copy()
decompose_result = seasonal_decompose(analysis, model="multiplicative")
trend = decompose_result.trend
seasonal = decompose_result.seasonal
residual = decompose_result.resid

decompose_result.plot()

plt.show()