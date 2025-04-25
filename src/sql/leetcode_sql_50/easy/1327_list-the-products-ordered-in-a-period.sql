/* https://leetcode.com/problems/list-the-products-ordered-in-a-period/

Table: Products

+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| product_id       | int     |
| product_name     | varchar |
| product_category | varchar |
+------------------+---------+
product_id is the primary key (column with unique values) for this table.
This table contains data about the company's products.
 

Table: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| order_date    | date    |
| unit          | int     |
+---------------+---------+
This table may have duplicate rows.
product_id is a foreign key (reference column) to the Products table.
unit is the number of products ordered in order_date.
 

Write a solution to get the names of products that have at least 100 units ordered in February 2020 and their amount.

Return the result table in any order. */

-- Write your PostgreSQL query statement below
SELECT product_name, SUM(unit) as unit FROM Orders
INNER JOIN Products USING(product_id)
WHERE order_date >= '2020-02-01' and order_date < '2020-03-01'
GROUP BY product_name
HAVING SUM(unit) > 99