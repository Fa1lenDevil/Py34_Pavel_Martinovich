-- CREATE TABLE Homework(
-- 	Code INT AUTO_INCREMENT NOT NULL,
--     model VARCHAR(50),
--     speed SMALLINT,
--     RAM SMALLINT,
--     hd REAL,
--     cd VARCHAR(10),
--     price FLOAT,
--     PRIMARY KEY(Code)
-- );

-- INSERT INTO Homework (model, speed, RAM, hd, cd, price)
-- VALUES 
-- ('lenovo', 3, 16, 1000, '16x', 1882.6),
-- ('HP', 4, 24, 750, '12x', 955.6),
-- ('Acer', 3, 8, 500, '14x', 1784.6),
-- ('Asus', 5, 32, 1500, '12x', 3281.6),
-- ('Aorus', 4, 64, 2000, '10x', 883.6);

-- select *
-- from Homework
-- WHERE price<400

-- SELECT model, speed, hd
-- from homework
-- WHERE RAM <= 16 and RAM >= 8

-- SELECT price FROM homework
-- WHERE hd < 1000
-- SET SQL_SAFE_UPDATES = 0;

-- UPDATE homework
-- set price = price*2
-- WHERE price > 400