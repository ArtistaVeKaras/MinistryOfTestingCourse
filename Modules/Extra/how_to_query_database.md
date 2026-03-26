# How to Query Your Database in Tests

![Querying a database from tests](https://res.cloudinary.com/dsuzv7xqn/image/upload/v1772460690/markdown-images/aiwqpk7cpwjmiva1exxq.png)

Short, practical guidance for running database queries from automated tests. Focus on reliability, isolation, and speed.

## Approaches

- **Direct SQL from tests:** Run queries directly using a DB client inside your test assertions. Fast and explicit, but couples tests to schema details.
- **Through the service/repository layer:** Use application code to exercise DB interactions; this stays closer to production behavior.
- **Fixtures & factories:** Use factories or fixtures to create deterministic test data and reduce boilerplate.

## Recommended libraries

- Postgres: `pg`
- MySQL: `mysql2`
- SQL Server: `mssql`
- SQLite: `better-sqlite3`

## Example (Node + pg)

```js
// Minimal example using Jest
const { Client } = require('pg');
let client;
beforeAll(async () => {
	client = new Client({ connectionString: process.env.TEST_DATABASE_URL });
	await client.connect();
});
afterAll(() => client.end());

test('creates a user record', async () => {
	// perform action that creates a user in your app
	const res = await client.query('SELECT * FROM users WHERE email = $1', ['test@example.com']);
	expect(res.rows.length).toBe(1);
});
```

## Playwright integration (UI → DB)

1. Connect to the test database in your Playwright/Jest setup.
2. Drive the UI (e.g., fill a form, submit).
3. Query the DB to verify the persisted state matches expectations.

## Use a dedicated test database

- Never run tests against production.
- Use an isolated test database instance (local, Docker, or ephemeral cloud DB).
- Prefer an environment variable like `TEST_DATABASE_URL` to switch easily.

## Keep state isolated and fast

- Use transactions with rollback when possible (begin a transaction in a test and roll it back in teardown).
- For broader integration tests, truncate or recreate only the necessary tables between tests.
- Seed small, focused datasets rather than full production dumps.

## Cleanup strategies

- Use `afterEach` to truncate affected tables or rollback the enclosing transaction.
- Rebuild schema or apply migrations in CI to guarantee a clean baseline when needed.

## When to add database tests

- After CRUD operations that change persistence.
- When the UI displays calculated or aggregated values derived from DB data.
- After bulk operations (imports, batch updates).
- When business rules span multiple tables or services.
- After migration scripts or schema changes.
- For financial or transactional flows where data integrity is critical.

## Quick checklist

- Use a test-only database instance.
- Prefer transactions + rollback for speed and isolation where possible.
- Keep tests deterministic and small.
- Avoid relying on production data or external services.
- Run DB migration step in CI before tests.

---

If you'd like, I can add a Playwright Jest setup snippet or transaction-rollback examples tailored to your stack.
