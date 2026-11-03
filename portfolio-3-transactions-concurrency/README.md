# Portfolio 3 — Transactions and concurrency

[`transactions.sql`](transactions.sql) demonstrates a transaction, a savepoint rollback, a commit, and a full rollback using a temporary table so the example does not alter hospital records. Execute sequentially in one pgAdmin session and capture output showing the final rows.

The final comments provide a two-session row-lock exercise using the sample nurse visit. In Session A, hold a `FOR UPDATE` lock; in Session B, update that same row and observe it wait; commit A and observe B continue. Roll back B to leave the booking unchanged. Do not execute both sessions as one script: concurrency is only observable with separate sessions. Record your actual observation and the isolation level. PostgreSQL's default is READ COMMITTED; row locks serialize conflicting writes to the same nurse visit, while unrelated rows can be updated concurrently.

Evidence still needed: screenshot/output for committed and rolled-back rows, and a screenshot or written observation of the two-session wait and release. Roll back the demonstration status change so the booking remains as it was.

