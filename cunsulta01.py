import mysql.connector
# 1. Conectar ao banco de dados
conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="netflix.db"
)

 # 2. Criar um objeto cursor para executar as queries
cursor = conexao.cursor()

consultas = {
    consulta01 - filmes e séries": """"
    select type, count(*) as quantidades 
    from netflix_titles 
    group by type;
    """,

    consulta02 - países": """
    select country, count(*) as quantidades 
    from netflix_titles 
    where country is not null
    group by country 
    order by country
    order by quantidades desc
    limit 10;
    """,

    consulta03 - generos: """
    select listed_in, count(*)s quantidades 
    from netflix_titles 
    where listed_in is not null
    group by listed_in
    order by 
    order by quantidades desc
    limit 10;
    """,
    consulta04 - ano de lançamento": """
    select release_year, count(*) as quantidades 
    from netflix_titles 
    where country is not null
    group by 
    order by 
    order by 
    quantidades desc
    limit 10;
    """,
    consulta05 - duracao": """
    select type, duration
    count(*) as quantidades 
    from netflix_titles 
    where duration is not null
    group by type duration
    order by quantidade desc
    quantidades desc
    limit 10;
    """,

}




