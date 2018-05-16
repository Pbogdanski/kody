DROP TABLE IF EXISTS tbFilm;
CREATE TABLE tbFilm
(
    id INTEGER PRIMARY KEY,
    name TEXT,
    genre TEXT,
    year INTEGER,
    imdb_rating NUMERIC,
);