/* https://leetcode.com/problems/queries-quality-and-percentage

Table: Queries

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| query_name  | varchar |
| result      | varchar |
| position    | int     |
| rating      | int     |
+-------------+---------+
This table may have duplicate rows.
This table contains information collected from some queries on a database.
The position column has a value from 1 to 500.
The rating column has a value from 1 to 5. Query with rating less than 3 is a poor query.
 

We define query quality as:

The average of the ratio between query rating and its position.

We also define poor query percentage as:

The percentage of all queries with rating less than 3.

Write a solution to find each query_name, the quality and poor_query_percentage.

Both quality and poor_query_percentage should be rounded to 2 decimal places.

Return the result table in any order. */

-- Write your PostgreSQL query statement below
SELECT query_name, 
    ROUND(AVG(rating/position::NUMERIC), 2) as quality,
    ROUND(AVG((rating < 3)::INT) * 100.0, 2) as poor_query_percentage
    -- ROUND(100.0 * count(query_name) FILTER (WHERE rating < 3) / count(query_name), 2) as poor_query_percentage
FROM Queries
GROUP BY query_name