--Create table unique_id with id as default 1 and unique
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

INSERT INTO unique_id (id, name) VALUES (89, "Best");