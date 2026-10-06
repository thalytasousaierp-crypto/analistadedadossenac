import mysql.connector
import pandas as pd

conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="dados_netflix"
)

query = """
SELECT *
FROM netflix1;
"""

df = pd.read_sql(query, conexao)

print(df.head())
print(df.info())
print(df.describe())

print(df['type'].value_counts())

print(df['release_year'].value_counts().sort_index())

print(df['country'].value_counts().head(10))

print(df['rating'].value_counts())

print(df['listed_in'].value_counts().head(10))

