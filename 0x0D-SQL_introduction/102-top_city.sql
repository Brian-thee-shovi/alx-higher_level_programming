-- displays the average temp of 3 cities
-- during july and august
-- ordered by temp desc

SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = 7 OR MONTH = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

