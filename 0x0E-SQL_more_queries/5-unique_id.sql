-- Script that creates table unqiue_id
CREATE TABLE IF NOT EXISTS unqiue_id (
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256)
);
