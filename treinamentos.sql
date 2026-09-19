-- CRIANDO MEU BANCO DE DADOS:

CREATE DATABASE meu_ecommerce;

USE meu_ecommerce;

-- CRIANDO ENTIDADES DE PRODUTOS:
CREATE TABLE Produtos(
id_produto VARCHAR(10),
nome VARCHAR(100),
categoria VARCHAR(50),
preco DECIMAL(8,2),
estoque INT
);
-- Remoção Tabelas/Conteúdo de Tabelas
DROP TABLE Produtos;

SET GLOBAL local_infile = 1; -- marcação de aceite para arquivos locais (passo extra 01 junto ao load data)

-- 'OPT_LOCAL_INFILE=1' -- (passo extra 02 junto ao load data) inserir na sua conexão local (edit da conexão >> Advanced >> Others)

LOAD DATA LOCAL INFILE 'C:/Users/nomenamaquina/caminhodiretorio/vendas_produtos.csv' -- Ajuste o caminho no seu banco local
INTO TABLE vendas_online.produtos
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n' -- Aqui: CR LF
IGNORE 1 ROWS -- Pula o cabeçalho 'id_produto,nome...'
(id_produto, nome, categoria, @preco_var, estoque) -- Mapeia colunas
SET preco = REPLACE(@preco_var, '.', '.'); -- Garante que o decimal seja lido corretamente


-- id_produto,nome,categoria,preco,estoque

-- CRIANDO ENTIDADE CLIENTE:
CREATE TABLE clientes (
id_cliente VARCHAR(10) PRIMARY KEY,
nome VARCHAR(100),
email VARCHAR(30)
);

-- DELETE FROM cliente WHERE id_cliente = "id_cliente';
CREATE TABLE pedidos(
id_pedido VARCHAR (10),
id_cliente VARCHAR (10),
Data_pedido DATETIME,
valor_total DECIMAL (10,2),
id_produto VARCHAR (10),
quantidade SMALLINT
);

LOAD DATA LOCAL INFILE 'C:/Users/"C:\Users\thalyta.martins\Documents\bigdata.py\analistadedadossenac-3\UC2\vendas_clientes.csv""' -- Ajuste o caminho no seu banco local
INTO TABLE meu_ecommerce.clientes
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n' -- Aqui: CR LF
IGNORE 1 ROWS -- Pula o cabeçalho 'id_produto,nome...'
(id_cliente, nome, email); -- Mapeia colunas
SET preco = REPLACE(@preco_var, '.', '.'); -- Garante que o decimal seja lido corretamente

-- OPÇÕES DE CONSTRUÇÃO DE CHAVES:
-- 1 - DESDE O CREATE TABLE:
CREATE TABLE pedidos (
 id_pedido INT auto_increment primary key,
 data_pedido DATE,
 valor_total DECIMAL(10, 2),
 id_cliente INT,
 id_produto INT,
 quantidade INT,
 FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
 FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
 );
 
 -- 2 - A PARTIR DE ALTER TABLE:
 -- 2.1 PK
 ALTER TABLE pedidos
ADD CONSTRAINT fk_pedidos_clientes
FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente);

ALTER TABLE produtos
ADD CONSTRAINT fk_pedidos_produtos
FOREIGN KEY (id_produto) REFERENCES produtos(id_produto);

ALTER TABLE produtos
ADD CONSTRAINT pk_produtos
PRIMARY KEY (id_produto);

ALTER TABLE clientes
ADD CONSTRAINT pk_cliente
PRIMARY KEY (id_cliente);

ALTER TABLE pedidos
ADD CONSTRAINT pk_pedidos
PRIMARY KEY (id_pedido);

-- 2.2 PK
 ALTER TABLE pedidos
ADD CONSTRAINT Pk_pedidos_clientes
FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente);

ALTER TABLE pedidos
ADD CONSTRAINT fk_pedidos_clientes
FOREIGN KEY (id_produto) REFERENCES produtos(id_produto);
