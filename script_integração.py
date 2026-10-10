import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns

# Conexão com o MySQL
conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="dados_netflix"
)

# Ler dados da tabela
query = """
SELECT *
FROM netflix1;
"""

df = pd.read_sql(query, conexao)

print(df.head())

# ---------------------------
# GRÁFICO 1 - Filmes x Séries
# ---------------------------

plt.figure(figsize=(6,4))

df['type'].value_counts().plot(
    kind='bar',
    color=['red', 'blue']
)

plt.title('Filmes x Séries')
plt.xlabel('Tipo')
plt.ylabel('Quantidade')
plt.show()

# ---------------------------
# GRÁFICO 2 - Top 10 países
# ---------------------------

plt.figure(figsize=(10,5))

df['country'].value_counts().head(10).plot(
    kind='bar',
    color='green'
)

plt.title('Top 10 Países')
plt.xlabel('País')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)

plt.show()

# ---------------------------
# GRÁFICO 3 - Lançamentos por ano
# ---------------------------

plt.figure(figsize=(12,5))

df['release_year'].value_counts()\
    .sort_index()\
    .plot(kind='line')

plt.title('Lançamentos por Ano')
plt.xlabel('Ano')
plt.ylabel('Quantidade')

plt.show()

conexao.close()

df['listed_in'].value_counts().head(10).plot(
    kind='bar',
    figsize=(10,5)
)

plt.title('Top 10 Categorias')
plt.show()

query = """
SELECT
    t.vote_average,
    t.popularity
FROM tmdb_5000_movies t
"""

df_tmdb = pd.read_sql(query, conexao)

sns.scatterplot(
    data=df_tmdb,
    x='vote_average',
    y='popularity'
)

plt.title('Popularidade x Nota')
plt.show()



