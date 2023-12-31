-- This script calculates the mean temperature for each city from the 'temperatures' table
-- Data is sourced from the 'hbtn_0c_0' database
SELECT city, AVG(value) AS avg_temp
FROM hbtn_0c_0.temperatures
GROUP BY city
ORDER BY avg_temp DESC;
