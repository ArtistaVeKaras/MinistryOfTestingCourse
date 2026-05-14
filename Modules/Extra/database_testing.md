# 7 Database Testing Scenarios

A consolidated reference of the core database‑testing scenarios, each describing the risk, what to validate, and a real‑world example.

## Scenario 1 — Data Integrity After Create

![Data Integrity Checks](https://res.cloudinary.com/dsuzv7xqn/image/upload/v1772457980/markdown-images/iuzm3w6rfwao5gj1ylni.png)

Ensuring that data submitted through the UI is stored accurately and completely in the database.

### What to check after Create

* Data is stored in the correct table
* Values match the correct columns
* Data types are preserved without truncation
* Timestamps are accurate and timezone‑safe
* Foreign key references are valid

Real‑world example
A user enters “123 Main St”, but the database stores “123 Main” because the column is limited to VARCHAR(10).

## Scenario 2 — Cascade Deletes

![Cascade Deletes](https://res.cloudinary.com/dsuzv7xqn/image/upload/v1772459423/markdown-images/g9fqj1idbpgngbi0pggr.png)

Validating how the system handles dependent records when a parent record is removed.

### What to check in Cascade Delete

* Child records are deleted or nullified correctly
* No orphaned records remain
* Join‑table relationships are cleaned up
* Soft deletes correctly update deleted_at
* Cascading rules do not remove unintended data

Real‑world example
Deleting a user account leaves behind orphaned order history, comments, or uploaded files.

### Scenario 3 — Concurrent Updates

![Concurrent Updates](https://res.cloudinary.com/dsuzv7xqn/image/upload/v1772459509/markdown-images/bjufghbz1py3wlatiqp4.png)

Ensuring the system behaves predictably when two users update the same record simultaneously.

### What to check in Concurrent Updates

* Conflict handling or “last write wins” is clearly defined
* No data corruption from simultaneous writes
* Optimistic locking returns clear, actionable errors
* Both users see the correct final state
* Audit logs capture both update attempts

Real‑world example
Two admins update a product price at the same time—one sets £19.99, the other £24.99—and the final stored value becomes unpredictable.

### Scenario 4 — Data Type Boundaries

![Data Type Boundaries](https://res.cloudinary.com/dsuzv7xqn/image/upload/v1772458277/markdown-images/goszjs4e12liirsa6hfg.png)

Testing how the system handles maximum and minimum values for each field.

### What data types to check

* Integer overflow is handled safely
* String length limits do not silently truncate
* Date ranges respect minimum and maximum boundaries
* Decimal precision is preserved
* Special characters are stored correctly

Real‑world example
The UI accepts “999999999”, but the database integer type overflows at 2,147,483,647, causing silent corruption.

### Scenario 5 — NULL Handling

![Null Handling](https://res.cloudinary.com/dsuzv7xqn/image/upload/v1772458563/markdown-images/zdnt6k59qoyzyfv27tlo.png)

Verifying how the system treats NULL values across required and optional fields.

### What to check in Null Handling

* Required fields reject NULL at the database level
* Optional fields handle NULL gracefully
* NULL vs empty string is treated consistently
* Queries involving NULL return correct results
* UI displays NULL values without breaking or showing literal “null”

Real‑world example
A user skips the phone number field, and the UI displays “null” instead of leaving it blank.

### Scenario 6 — Index Performance

![Index Performance](https://res.cloudinary.com/dsuzv7xqn/image/upload/v1772458644/markdown-images/uhwd22olxznby0bcj2bm.png)

Ensuring that queries scale correctly as data volume increases.

### What to check in Index Performance

* Search queries use appropriate indexes
* Performance is validated at realistic data volumes
* Slow queries are identified using EXPLAIN plans
* Composite indexes support frequent joins
* Full table scans are avoided on large datasets

Real‑world example
A search query works instantly in development with 50 records but takes 8 seconds in production with 500,000 records.

### Scenario 7 — Transaction Rollbacks

![Transactions Rollbacks](https://res.cloudinary.com/dsuzv7xqn/image/upload/v1772458825/markdown-images/xvyrfozdn1kcc4oxpxer.png)

Ensuring multi‑step operations roll back cleanly when a failure occurs.

### What to check in Transactions Rollbacks

* Partial commits do not leave inconsistent data
* Payment failures correctly roll back order creation
* Multi‑table operations behave atomically
* Error handling triggers proper rollback
* Retry logic does not create duplicate records

Real‑world example
A payment gateway times out after the order is created. The order remains stuck in “pending” forever, with no refund and no cleanup.
