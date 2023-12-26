import pandas as pd

#Importando dados
data = pd.read_excel("data/VendaCarros.xlsx")
print(data)

#Lista os primeiros registros
print(data.head())

#lista dos ultimos
print(data.tail())

#contagem de valor por fabricantes
print(data["Fabricante"].value_counts())

