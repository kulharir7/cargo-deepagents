# GraphQL Guide

## Schema Definition

type User {
    id: ID!
    email: String!
    name: String
    posts: [Post!]!
}

type Post {
    id: ID!
    title: String!
    content: String!
    author: User!
}

type Query {
    user(id: ID!): User
    users(limit: Int, offset: Int): [User!]!
    search(query: String!): [Post!]!
}

type Mutation {
    createUser(input: CreateUserInput!): User!
    updateUser(id: ID!, input: UpdateUserInput!): User!
    deleteUser(id: ID!): Boolean!
}

## Best Practices

1. Use non-nullable types where possible
2. Implement pagination for lists
3. Use input types for mutations
4. Add descriptions to all fields
5. Implement error handling
6. Use DataLoader for N+1 problem
