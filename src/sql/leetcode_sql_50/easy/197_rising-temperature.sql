/* https://leetcode.com/problems/rising-temperature

Table: Weather

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this table.
There are no different rows with the same recordDate.
This table contains information about the temperature on a certain day.
 

Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order. */

-- Solution 1
SELECT w1.id as Id FROM Weather w1
INNER JOIN Weather w2 ON w1.recordDate = w2.recordDate + 1
WHERE w1.temperature > w2.temperature;

-- Solution 2
SELECT w2.id as Id FROM Weather w1
CROSS JOIN Weather w2
WHERE w2.recordDate = w1.recordDate + 1 AND w2.temperature > w1.temperature;

-- Solution 3
SELECT Id FROM (
    SELECT
        id as Id,
        recordDate,
        temperature,
        LAG(recordDate) OVER (ORDER BY recordDate) as previous_date,
        LAG(temperature) OVER (ORDER BY recordDate) as previous_temperature
    FROM Weather
) as sub
WHERE recordDate - previous_date = 1 AND sub.temperature > sub.previous_temperature;
