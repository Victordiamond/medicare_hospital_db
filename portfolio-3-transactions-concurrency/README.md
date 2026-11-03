# Portfolio 3 — Transactions and concurrency

The temporary-table demonstration was run in pgAdmin on 3 November 2026. It inserted a committed example, rolled back the optional row to a savepoint, committed, then inserted a third row and fully rolled it back. A follow-up `SELECT * FROM transaction_demo ORDER BY event_id` returned exactly one row: `1, committed example`. The observed CSV is in [`../evidence/portfolio-3/transaction-final-state.csv`](../evidence/portfolio-3/transaction-final-state.csv).

This verifies the transaction/savepoint/full-rollback result for the current pgAdmin session. The table is temporary and contains no hospital records.

The separate two-session row-lock exercise is still untested. In Session A, hold a `FOR UPDATE` lock on the sample nurse visit; in Session B, update that same row and observe the wait; commit A and observe B continue; roll back B. Record only what is observed and the isolation level.

