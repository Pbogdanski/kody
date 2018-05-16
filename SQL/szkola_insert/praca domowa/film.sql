DROP TABLE IF EXISTS tbFilm;
CREATE TABLE tbFilm
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    genre TEXT,
    year DATE,
    imdb_rating NUMERIC,
);