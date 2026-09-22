QNO 2: CUSTOMER AND ORDER MANAGEMENT(3.5 marks)

There are two tables: `customer` and `orders`.

The `orders.customer_id` column is a FOREIGN KEY referencing `customer.customer_id`.

---

## TABLE 1: customer

Columns and Data Types:

customer_id     INT           PRIMARY KEY
customer_name   VARCHAR(50)
city            VARCHAR(50)

Data:

customer_id    customer_name    city
1              Amit             Indore
2              Rahul            Pune
3              Priya            Mumbai
4              Neha             Delhi
5              Karan            Bhopal
6              Sneha            Jaipur

---

## TABLE 2: orders

Columns and Data Types:

order_id       INT             PRIMARY KEY
order_date     DATE
amount         DECIMAL(10,2)
customer_id    INT             FOREIGN KEY

Relationship:

orders.customer_id → customer.customer_id

Data:

order_id    order_date    amount      customer_id
101         2026-01-10    25000       1
102         2026-01-15    18000       2
103         2026-02-05    35000       1
104         2026-02-10    12000       3
105         2026-02-15    45000       4
106         2026-03-01    22000       2
107         2026-03-05    50000       3
108         2026-03-10    15000       1
109         2026-03-15    30000       5

==================================================
QUESTIONS
=========

Q1. Display customer ID, customer name, city, order ID and order amount for all customers who have placed orders.

Q2. Display each customers name and the total amount spent by that customer.

Q3. Display the customer name and total amount spent by customers whose total purchase amount is greater than 40000.

Q4. Display the details of orders whose amount is greater than the average order amount of all orders.

Use a SUBQUERY.

Q5. Display the customer name, city and order amount for the order(s) having the highest order amount.

Use a SUBQUERY and JOIN.

Q6. Display the details of customers who have placed at least one order having an amount greater than the average order amount.

Use a SUBQUERY and JOIN.

Q7. Display the customer name and their highest order amount, but display only those customers whose highest order amount is greater than the average order amount of all orders.

Use JOIN, GROUP BY and SUBQUERY.

==================================================





















mysql> CREATE TABLE customr( customer_id INT PRIMARY KEY, customer_name VARCHAR(50),  city
VARCHAR(50));
Query OK, 0 rows affected (0.36 sec)

mysql> RENAME TABLE customr TO customer;
Query OK, 0 rows affected (0.29 sec)

mysql> DESC customer;
+---------------+-------------+------+-----+---------+-------+
| Field         | Type        | Null | Key | Default | Extra |
+---------------+-------------+------+-----+---------+-------+
| customer_id   | int         | NO   | PRI | NULL    |       |
| customer_name | varchar(50) | YES  |     | NULL    |       |
| city          | varchar(50) | YES  |     | NULL    |       |
+---------------+-------------+------+-----+---------+-------+
3 rows in set (0.01 sec)

mysql> INSERT INTO customer VALUES
    -> (1, 'Amit', 'Indore'),
    -> (2, 'Rahul', 'Pune'),
    -> (3, 'Priya', 'Mumbai'),
    -> (4, 'Neha', 'Delhi'),
    -> (5, 'Karan', 'Bhopal'),
    -> (6, 'Sneha', 'Jaipur');
Query OK, 6 rows affected (0.11 sec)
Records: 6  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM customer;
+-------------+---------------+--------+
| customer_id | customer_name | city   |
+-------------+---------------+--------+
|           1 | Amit          | Indore |
|           2 | Rahul         | Pune   |
|           3 | Priya         | Mumbai |
|           4 | Neha          | Delhi  |
|           5 | Karan         | Bhopal |
|           6 | Sneha         | Jaipur |
+-------------+---------------+--------+
6 rows in set (0.00 sec)

mysql> CREATE TABLE orders ( order_id INT PRIMARY KEY, order_date DATE, amount DECIMAL(10,2), customer_id INT, FOREIGN KEY (customer_id) REFERENCES customer( customer_id));
ERROR 1050 (42S01): Table 'orders' already exists
mysql> 
mysql> 
mysql> DROP TABLE orders;
Query OK, 0 rows affected (0.25 sec)

mysql> CREATE TABLE orders ( order_id INT PRIMARY KEY, order_date DATE, amount DECIMAL(10,2), customer_id INT, FOREIGN KEY (customer_id) REFERENCES customer( customer_id));
Query OK, 0 rows affected (0.44 sec)

mysql> DESC orders;
+-------------+---------------+------+-----+---------+-------+
| Field       | Type          | Null | Key | Default | Extra |
+-------------+---------------+------+-----+---------+-------+
| order_id    | int           | NO   | PRI | NULL    |       |
| order_date  | date          | YES  |     | NULL    |       |
| amount      | decimal(10,2) | YES  |     | NULL    |       |
| customer_id | int           | YES  | MUL | NULL    |       |
+-------------+---------------+------+-----+---------+-------+
4 rows in set (0.00 sec)

mysql> INSERT INTO orders VALUES
    -> (101, '2026-01-10', 25000, 1),
    -> (102, '2026-01-15', 18000, 2),
    -> (103, '2026-02-05', 35000, 1),
    -> (104, '2026-02-10', 12000, 3),
    -> (105, '2026-02-15', 45000, 4),
    -> (106, '2026-03-01', 22000, 2),
    -> (107, '2026-03-05', 50000, 3),
    -> (108, '2026-03-10', 15000, 1),
    -> (109, '2026-03-15', 30000, 5);
Query OK, 9 rows affected (0.10 sec)
Records: 9  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM orders;
+----------+------------+----------+-------------+
| order_id | order_date | amount   | customer_id |
+----------+------------+----------+-------------+
|      101 | 2026-01-10 | 25000.00 |           1 |
|      102 | 2026-01-15 | 18000.00 |           2 |
|      103 | 2026-02-05 | 35000.00 |           1 |
|      104 | 2026-02-10 | 12000.00 |           3 |
|      105 | 2026-02-15 | 45000.00 |           4 |
|      106 | 2026-03-01 | 22000.00 |           2 |
|      107 | 2026-03-05 | 50000.00 |           3 |
|      108 | 2026-03-10 | 15000.00 |           1 |
|      109 | 2026-03-15 | 30000.00 |           5 |
+----------+------------+----------+-------------+
9 rows in set (0.00 sec)
























mysql> SELECT c.customer_id, c.customer_name, c.city, o.order_id, o.amount FROM customer AS c JOIN orders AS o ON o.customer_id = c.customer_id;
+-------------+---------------+--------+----------+----------+
| customer_id | customer_name | city   | order_id | amount   |
+-------------+---------------+--------+----------+----------+
|           1 | Amit          | Indore |      101 | 25000.00 |
|           1 | Amit          | Indore |      103 | 35000.00 |
|           1 | Amit          | Indore |      108 | 15000.00 |
|           2 | Rahul         | Pune   |      102 | 18000.00 |
|           2 | Rahul         | Pune   |      106 | 22000.00 |
|           3 | Priya         | Mumbai |      104 | 12000.00 |
|           3 | Priya         | Mumbai |      107 | 50000.00 |
|           4 | Neha          | Delhi  |      105 | 45000.00 |
|           5 | Karan         | Bhopal |      109 | 30000.00 |
+-------------+---------------+--------+----------+----------+
9 rows in set (0.00 sec)









mysql> SELECT c.customer_name, SUM(o.amount) FROM customer AS c JOIN orders AS o ON o.customer_id = c.customer_id GROUP BY c.customer_name;
+---------------+---------------+
| customer_name | SUM(o.amount) |
+---------------+---------------+
| Amit          |      75000.00 |
| Rahul         |      40000.00 |
| Priya         |      62000.00 |
| Neha          |      45000.00 |
| Karan         |      30000.00 |
+---------------+---------------+
5 rows in set (0.01 sec)






mysql> SELECT c.customer_name, SUM(o.amount) FROM customer AS c JOIN orders AS o ON o.customer_id = c.customer_id GROUP BY c.customer_name HAVING SUM(o.amount) > 40000;
+---------------+---------------+
| customer_name | SUM(o.amount) |
+---------------+---------------+
| Amit          |      75000.00 |
| Priya         |      62000.00 |
| Neha          |      45000.00 |
+---------------+---------------+
3 rows in set (0.00 sec)









mysql> SELECT * FROM orders WHERE amount > (SELECT AVG(o.amount) FROM orders AS o);
+----------+------------+----------+-------------+
| order_id | order_date | amount   | customer_id |
+----------+------------+----------+-------------+
|      103 | 2026-02-05 | 35000.00 |           1 |
|      105 | 2026-02-15 | 45000.00 |           4 |
|      107 | 2026-03-05 | 50000.00 |           3 |
|      109 | 2026-03-15 | 30000.00 |           5 |
+----------+------------+----------+-------------+







mysql> SELECT c.customer_name, c.city, o.amount FROM customer AS c JOIN orders AS o ON o.customer_id = c.customer_id WHERE o.amount = (SELECT MAX(amount) FROM orders);
+---------------+--------+----------+
| customer_name | city   | amount   |
+---------------+--------+----------+
| Priya         | Mumbai | 50000.00 |
+---------------+--------+----------+
1 row in set (0.00 sec)









mysql> SELECT * FROM customer AS c JOIN orders AS o ON o.customer_id = c.customer_id WHERE
amount > (SELECT AVG(amount) FROM orders);
+-------------+---------------+--------+----------+------------+----------+-------------+
| customer_id | customer_name | city   | order_id | order_date | amount   | customer_id |
+-------------+---------------+--------+----------+------------+----------+-------------+
|           1 | Amit          | Indore |      103 | 2026-02-05 | 35000.00 |           1 |
|           4 | Neha          | Delhi  |      105 | 2026-02-15 | 45000.00 |           4 |
|           3 | Priya         | Mumbai |      107 | 2026-03-05 | 50000.00 |           3 |
|           5 | Karan         | Bhopal |      109 | 2026-03-15 | 30000.00 |           5 |
+-------------+---------------+--------+----------+------------+----------+-------------+
4 rows in set (0.00 sec)








mysql> SELECT c.customer_name, MAX(o.amount) FROM customer AS c JOIN orders AS o ON o.customer_id = c.customer_id GROUP BY c.customer_name HAVING MAX(o.amount) > (SELECT AVG(amount)
FROM orders);
+---------------+---------------+
| customer_name | MAX(o.amount) |
+---------------+---------------+
| Amit          |      35000.00 |
| Priya         |      50000.00 |
| Neha          |      45000.00 |
| Karan         |      30000.00 |
+---------------+---------------+
4 rows in set (0.03 sec)