-- script that displays the average temperature by city ordered by temperature (descending)
SELECT city, AVG(values) AS city, avg_temp
FROM temperatures GROUP BY city DESC;
