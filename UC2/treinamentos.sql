 DQL - vendas_online
*******************************************************************************/

-- SELEÇÃO E FILTROS SIMPLES

-- Seleção Total: Seleciona todas as colunas e todas as linhas da tabela.
SELECT * FROM produtos;

-- Seleção de Colunas Específicas e Ordenação: 
-- Filtra apenas nome e preço, ordenando do mais caro para o mais barato.
SELECT nome, preco 
FROM produtos 
ORDER BY preco DESC;

-- Filtro com Condição (WHERE):
-- Restringe os resultados a uma categoria e a um preço mínimo.
SELECT * FROM produtos 
WHERE categoria = 'Eletrônicos' AND preco > 1000;


-- LIKE (BUSCA POR PADRÕES)

-- Busca que Inicia com um Termo:
-- O '%' no final indica que qualquer texto pode seguir após 'Smartphone'.
SELECT * FROM produtos 
WHERE nome LIKE 'Smartphone%';

-- Busca que Termina com um Termo:
-- Encontra clientes que utilizam domínios de e-mail específicos.
SELECT * FROM clientes 
WHERE email LIKE '%@email.com';

-- Busca de Termo em Qualquer Posição (Contém):
-- Encontra qualquer registro que possua a palavra 'Gamer' no nome.
SELECT * FROM produtos 
WHERE nome LIKE '%Gamer%';

-- Busca com Caractere Único (_):
-- O '_' exige exatamente UM caractere naquela posição (Ex: Ana, Ani).
SELECT * FROM clientes 
WHERE nome LIKE 'An_';

-- Operador NOT LIKE:
-- Retorna todos os produtos que NÃO pertencem à categoria 'Eletrônicos'.
SELECT * FROM produtos 
WHERE categoria NOT LIKE 'Eletrônicos%';


-- AGREGAÇÕES E AGRUPAMENTOS

-- Funções de Agregação:
-- Calcula o total de registros, a soma financeira e a média de valor dos pedidos.
SELECT 
    COUNT(*) AS total_pedidos, 
    SUM(valor_total) AS faturamento_total, 
    AVG(valor_total) AS ticket_medio 
FROM pedidos;

-- Agrupamento com Filtro de Grupo (GROUP BY & HAVING):
-- Agrupa produtos por categoria, calcula média e filtra apenas grupos com mais de 5 itens.
SELECT categoria, COUNT(*) AS qtd_produtos, AVG(preco) AS preco_medio
FROM produtos
GROUP BY categoria
HAVING qtd_produtos > 5;


-- RELACIONAMENTOS (JOINS)

-- Inner Join Simples:
-- Combina pedidos e clientes onde o ID do cliente coincide em ambas as tabelas.
SELECT p.id_pedido, c.nome AS nome_cliente, p.data_pedido, p.valor_total
FROM pedidos p
INNER JOIN clientes c ON p.id_cliente = c.id_cliente;

-- Join Múltiplo (Relatório Completo):
-- Conecta as três tabelas para identificar o cliente, o produto e os detalhes da venda.
SELECT 
    p.id_pedido, 
    c.nome AS cliente, 
    pr.nome AS produto, 
    p.quantidade,
    p.valor_total
FROM pedidos p
JOIN clientes c ON p.id_cliente = c.id_cliente
JOIN produtos pr ON p.id_produto = pr.id_produto;


-- CTEs, WINDOW FUNCTIONS E SUBQUERIES

-- CTE (Common Table Expressions):
-- Cria uma tabela temporária nomeada para organizar cálculos antes da consulta final.
WITH VendasPorCliente AS (
    SELECT id_cliente, SUM(valor_total) AS total_gasto
    FROM pedidos
    GROUP BY id_cliente
)
SELECT c.nome, v.total_gasto
FROM clientes c
JOIN VendasPorCliente v ON c.id_cliente = v.id_cliente
WHERE v.total_gasto > 2000;

-- Window Function (RANK):
-- Cria um ranking de pedidos por valor sem a necessidade de agrupar as linhas.
SELECT 
    id_pedido, 
    data_pedido, 
    valor_total,
    RANK() OVER (ORDER BY valor_total DESC) AS ranking_valor
FROM pedidos;

-- Subquery Correlacionada:
-- Seleciona produtos cujo preço é maior que a média da sua respectiva categoria.
SELECT nome, preco, categoria
FROM produtos p1
WHERE preco > (
    SELECT AVG(preco) 
    FROM produtos p2 
    WHERE p1.categoria = p2.categoria
);



