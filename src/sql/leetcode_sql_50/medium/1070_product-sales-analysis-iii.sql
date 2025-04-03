/* https://leetcode.com/problems/product-sales-analysis-iii

Table: Sales

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(sale_id, year) is the primary key (combination of columns with unique values) of this table.
product_id is a foreign key (reference column) to Product table.
Each row of this table shows a sale on the product product_id in a certain year.
Note that the price is per unit.

Table: Product

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the product name of each product.

Write a solution to select the product id, year, quantity, and price for the first year of every product sold. If any product is bought multiple times in its first year, return all sales separately.

Return the resulting table in any order. */

-- Write your PostgreSQL query statement below
SELECT s1.product_id, first_year, quantity, price FROM Sales s1
INNER JOIN (
    SELECT product_id, MIN(year) as first_year FROM Sales
    GROUP BY product_id
) s2 ON s1.product_id = s2.product_id AND s1.year = s2.first_year