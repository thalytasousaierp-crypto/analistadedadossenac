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

