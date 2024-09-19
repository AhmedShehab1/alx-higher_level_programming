-- displays the avg temperature (fahrenheit) by city ordered by temp (desceding)

SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
