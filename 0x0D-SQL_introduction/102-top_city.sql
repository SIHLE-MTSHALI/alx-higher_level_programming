-- Display top 3 cities by temperature during July and August
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE MONTH(record_date) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

