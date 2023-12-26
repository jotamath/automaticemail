import pandas as pd

#Importando dados
data = pd.read_excel("data/VendaCarros.xlsx")
# print(type(data))

#Selecionando colunas específicas do dataframe
df = data[["Fabricante", "ValorVenda","Ano"]]
print(df)

#criando a tabela pivô
pivot_table = df.pivot_table(
    index="Ano",
    columns="Fabricante",
    values="ValorVenda",
    aggfunc="sum"
)

print(pivot_table)

#exportando tabela em arquivo excel
pivot_table.to_excel("data/pivot_table.xlsx","Relatorio")