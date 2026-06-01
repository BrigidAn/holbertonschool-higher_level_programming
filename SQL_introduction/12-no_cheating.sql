-- Insert initial values into second_table
INSERT INTO second_table(id, name, score)
VALUES(1, 'John', 10),(2, 'Bob', 10),(3, 'George', 8),(4,'Alex',3);

-- Update Bob's score to 10
UPDATE second_table
SET score = 10
WHERE name = 'Bob';