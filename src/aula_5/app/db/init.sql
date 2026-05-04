-- app/db/init.sql
DROP TABLE IF EXISTS items;

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    descricao TEXT NOT NULL
);