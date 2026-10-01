CREATE DATABASE dados_netflix;

USE dados_netflix;

CREATE TABLE netflix1(
show_id VARCHAR (10),
type VARCHAR (20),
title VARCHAR(255),
    director TEXT,
    country VARCHAR(100),
    date_added VARCHAR(50),
    release_year INT,
    rating VARCHAR(20),
    duration VARCHAR(50),
    listed_in TEXT
);

SELECT type, COUNT(*) AS quantidade
FROM netflix
GROUP BY type;

