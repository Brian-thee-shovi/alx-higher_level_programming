-- updates the score of bob to 10 in the second_table
UPDATE second_table
SET score = 10
WHERE name = "Bob";

SELECT score, name
FROM second_table
ORDER BY score DESC

