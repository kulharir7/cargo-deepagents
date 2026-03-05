# SQL Query Patterns

## CRUD Operations

-- Create
INSERT INTO users (name, email) VALUES ('John', 'john@example.com');

-- Read
SELECT * FROM users WHERE id = 1;

-- Update
UPDATE users SET name = 'Jane' WHERE id = 1;

-- Delete
DELETE FROM users WHERE id = 1;

## JOINs

-- Inner Join
SELECT u.name, o.total
FROM users u
INNER JOIN orders o ON u.id = o.user_id;

-- Left Join
SELECT u.name, o.total
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- Aggregation
SELECT category, COUNT(*) as count, AVG(price) as avg_price
FROM products
GROUP BY category
HAVING count > 10
ORDER BY count DESC;

## Indexes

CREATE INDEX idx_email ON users(email);
CREATE INDEX idx_created ON users(created_at);
DROP INDEX idx_email ON users;
