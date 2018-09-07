DROP TABLE IF EXISTS filmy;
CREATE TABLE filmy
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    genre TEXT DEFAULT '',
    year INTEGER,
    imdb_rating DECIMAL,
);