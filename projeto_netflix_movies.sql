CREATE DATABASE dados_netflix;

USE dados_netflix;

CREATE TABLE netflix1 (
    show_id VARCHAR(20),
    type VARCHAR(20),
    title VARCHAR(255),
    director TEXT,
    cast_members TEXT,
    country TEXT,
    date_added VARCHAR(50),
    release_year INT,
    rating VARCHAR(20),
    duration VARCHAR(50),
    listed_in TEXT,
    description TEXT
);
CREATE TABLE netflix (
    show_id VARCHAR(10),
    type VARCHAR(20),
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
FROM netflix1
GROUP BY type;

SELECT country, COUNT(*) AS quantidade
FROM netflix1
WHERE country IS NOT NULL
GROUP BY country
ORDER BY quantidade DESC
LIMIT 10;

SELECT release_year, COUNT(*) AS quantidade
FROM netflix1
GROUP BY release_year
ORDER BY release_year;

SELECT rating, COUNT(*) AS quantidade
FROM netflix1
GROUP BY rating
ORDER BY quantidade DESC;

SELECT COUNT(*) AS total
FROM netflix1
WHERE release_year >= 2015;


CREATE TABLE tmdb_5000_movies (
    budget BIGINT,
    genres TEXT,
    homepage TEXT,
    id INT,
    keywords TEXT,
    original_language VARCHAR(10),
    original_title VARCHAR(255),
    overview TEXT,
    popularity DECIMAL(12,6),
    production_companies TEXT,
    production_countries TEXT,
    release_date DATE,
    revenue BIGINT,
    runtime INT,
    spoken_languages TEXT,
    status VARCHAR(50),
    tagline TEXT,
    title VARCHAR(255),
    vote_average DECIMAL(4,2),
    vote_count INT
);

SELECT
    n.show_id,
    n.title,
    n.type,
    n.release_year,
    t.id AS tmdb_id,
    t.popularity,
    t.vote_average,
    t.revenue,
    t.budget
FROM netflix1 n
INNER JOIN tmdb_5000_movies t
    ON n.title = t.title;
    
    SELECT
    n.title,
    n.release_year,
    t.popularity,
    t.vote_average
FROM netflix1 n
INNER JOIN tmdb_5000_movies t
    ON n.title = t.title
ORDER BY t.vote_average DESC;

SELECT n.title
FROM netflix1 n
LEFT JOIN tmdb_5000_movies t
    ON n.title = t.title
WHERE t.title IS NULL;

ALTER TABLE netflix1
ADD COLUMN tmdb_id INT;

UPDATE netflix1 n
JOIN tmdb_5000_movies t
    ON n.title = t.title
SET n.tmdb_id = t.id;

ALTER TABLE netflix1
ADD CONSTRAINT fk_tmdb
FOREIGN KEY (tmdb_id)
REFERENCES tmdb_5000_movies(id);

ALTER TABLE tmdb_5000_movies
ADD PRIMARY KEY (id);
    
