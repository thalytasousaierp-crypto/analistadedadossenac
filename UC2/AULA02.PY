#LDC
#ILOC
#QUERY

import pandas as pd 
import numpy as np

filmes = {
    'título':["Lagoa Azul", "Agente Secreto", "Gênio Indomável","A Freira","Brinquedo Assassino","Top gun"],
    'categoria':["Romance", "Ação", "Drama","Terror", "Comédia", "Aventura"],
    'ano':["1980","2025","1997","2022","1995","1986"],
    'Faturamento':[6, 5, 4, 5, 5, 3]
}

indices = ['A','B','C','D','E','F']
tabela_filmes = pd.DataFrame (filmes, index=indices)

#print(filmes)
#print(type(filmes))
print(tabela_filmes)
#print(type(tabela_filmes))
#print(tabela_filmes.iloc[-1])
print('-'*20)
print(tabela_filmes.iloc[1:3])
print(tabela_filmes.loc['B':'E'])
#print('-'*20)
print(tabela_filmes.loc['B'])
consulta1 = tabela_filmes.query("Faturamento == 5.5")
print(consulta1)
#<> <:>= == != and or not in



