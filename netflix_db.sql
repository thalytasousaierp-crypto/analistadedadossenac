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
FROM netflix
GROUP BY type;

SELECT country, COUNT(*) AS quantidade
FROM netflix
WHERE country IS NOT NULL
GROUP BY country
ORDER BY quantidade DESC
LIMIT 10;

SELECT release_year, COUNT(*) AS quantidade
FROM netflix
GROUP BY release_year
ORDER BY release_year;

SELECT rating, COUNT(*) AS quantidade
FROM netflix
GROUP BY rating
ORDER BY quantidade DESC;

SELECT COUNT(*) AS total
FROM netflix
WHERE release_year >= 2015;

CREATE DATABASE netflix_db;