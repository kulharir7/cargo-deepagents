---
name: database-agent
description: "INVOKE THIS SKILL for database tasks. Triggers: 'SQL', 'NoSQL', 'query', 'schema', 'migration', 'database'."
---

<oneliner>
Database expert for SQL, NoSQL, schema design, migrations, and query optimization.
</oneliner>

<setup>
## Supported Databases
- **SQL**: SQLite, PostgreSQL, MySQL
- **NoSQL**: MongoDB, Redis
- **Search**: Elasticsearch

## Dependencies
`ash
pip install psycopg2-binary pymongo redis elasticsearch
`
</setup>

<capabilities>
- SQL query optimization
- Schema design
- Data migration
- Index optimization
- Query analysis
- Connection pooling
</capabilities>

<sql>
`sql
-- Create table with indexes
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW()
);

-- Create index for performance
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_created ON users(created_at DESC);

-- Complex query with JOIN
SELECT u.name, COUNT(o.id) as order_count, SUM(o.total) as total_spent
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at > NOW() - INTERVAL '30 days'
GROUP BY u.id
HAVING COUNT(o.id) > 0
ORDER BY total_spent DESC
LIMIT 10;

-- Explain analyze
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'test@example.com';
`
</sql>

<mongodb>
`javascript
// Aggregation pipeline
db.orders.aggregate([
  { match: { status: "completed" } },
  { group: { 
      _id: "userId", 
      totalSpent: { sum: "amount" },
      orderCount: { sum: 1 }
  }},
  { sort: { totalSpent: -1 } },
  { limit: 10 }
]);

// Index creation
db.users.createIndex({ email: 1 }, { unique: true });
db.orders.createIndex({ userId: 1, createdAt: -1 });
`
</mongodb>

<migration>
`sql
-- Migration up
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    total DECIMAL(10, 2),
    status VARCHAR(20) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT NOW()
);

-- Migration down
DROP TABLE IF EXISTS orders;
`
</migration>

<tips>
1. Use indexes for frequently queried columns
2. Avoid SELECT * in production
3. Use connection pooling
4. Monitor slow queries
5. Regular backups
6. Use transactions for related operations
</tips>

<triggers>
- 'database', 'SQL', 'NoSQL', 'query'
- 'schema', 'migration', 'index', 'table'
- 'MongoDB', 'PostgreSQL', 'MySQL', 'Redis'
</triggers>
