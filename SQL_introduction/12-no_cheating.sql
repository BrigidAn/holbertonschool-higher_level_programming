insert into second_table(id, name, score)
values(1, 'John', 10),(2, 'Bob', 10),(3, 'George', 8),(4,'Alex',3);

update second_table
SET score = 10
where name = 'Bob';