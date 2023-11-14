-- Script to display the maximum temperature for each state, ordered by state name
SELECT state, MAX(temperature) AS max_temp
FROM hbtn_0c_0.temperatures
GROUP BY state
ORDER BY state;
