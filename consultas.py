import mysql.connector

# Conectar ao banco
conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="dados_netflix"
)

cursor = conexao.cursor()

consultas = {

    "Consulta 1 - Filmes e Séries": """
    SELECT type, COUNT(*) AS quantidade
    FROM netflix1
    GROUP BY type;
    """,

    "Consulta 2 - Top 10 Países": """
    SELECT country, COUNT(*) AS quantidade
    FROM netflix1
    WHERE country IS NOT NULL
    GROUP BY country
    ORDER BY quantidade DESC
    LIMIT 10;
    """,

    "Consulta 3 - Top 10 Categorias": """
    SELECT listed_in, COUNT(*) AS quantidade
    FROM netflix1
    WHERE listed_in IS NOT NULL
    GROUP BY listed_in
    ORDER BY quantidade DESC
    LIMIT 10;
    """,

    "Consulta 4 - Lançamentos por Ano": """
    SELECT release_year, COUNT(*) AS quantidade
    FROM netflix1
    GROUP BY release_year
    ORDER BY release_year DESC;
    """,

    "Consulta 5 - Duração por Tipo": """
    SELECT type, duration, COUNT(*) AS quantidade
    FROM netflix1
    WHERE duration IS NOT NULL
    GROUP BY type, duration
    ORDER BY quantidade DESC
    LIMIT 10;
    """,

    "Consulta 6 - Netflix x TMDB": """
    SELECT
        n.title,
        n.release_year,
        t.popularity,
        t.vote_average,
        t.revenue,
        t.budget
    FROM netflix1 n
    INNER JOIN tmdb_5000_movies t
        ON TRIM(LOWER(n.title)) = TRIM(LOWER(t.title))
    ORDER BY t.vote_average DESC;
    """
}

# Executar consultas
for nome, sql in consultas.items():

    print("\n" + "=" * 60)
    print(nome)
    print("=" * 60)

    cursor.execute(sql)

    for linha in cursor.fetchall():
        print(linha)

cursor.close()
conexao.close()

