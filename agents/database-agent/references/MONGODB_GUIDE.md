# MongoDB Guide

## CRUD Operations

// Create
db.users.insertOne({ name: 'John', email: 'john@example.com' })

// Read
db.users.findOne({ _id: ObjectId('...') })
db.users.find({ age: { gte: 18 } })

// Update
db.users.updateOne(
    { _id: ObjectId('...') },
    { set: { name: 'Jane' } }
)

// Delete
db.users.deleteOne({ _id: ObjectId('...') })

## Aggregation Pipeline

db.orders.aggregate([
    { match: { status: 'completed' } },
    { group: { _id: 'user_id', total: { sum: 'amount' } } },
    { sort: { total: -1 } },
    { limit: 10 }
])

## Indexes

db.users.createIndex({ email: 1 }, { unique: true })
db.users.createIndex({ name: 1, email: 1 })
db.orders.createIndex({ created_at: -1 })
