# Portfolio 3 — Transactions and concurrency

The temporary-table demonstration was run in pgAdmin on 3 November 2026. It inserted a committed example, rolled back the optional row to a savepoint, committed, then inserted a third row and fully rolled it back. A follow-up `SELECT * FROM transaction_demo ORDER BY event_id` returned exactly one row: `1, committed example`. The observed CSV is in [`../evidence/portfolio-3/transaction-final-state.csv`](../evidence/portfolio-3/transaction-final-state.csv).

This verifies the transaction/savepoint/full-rollback result for the current pgAdmin session. The table is temporary and contains no hospital records.

The separate row-lock exercise was then observed in pgAdmin on 3 November 2026. Session A ran `BEGIN` and selected nurse visit 1 `FOR UPDATE`. Session B began a transaction and attempted to set its status to `in_progress`; pgAdmin showed that the command was still in progress while A held the lock. A committed, and B's update completed after about 26 seconds. B was rolled back. An extra query tool had also queued an identical update unintentionally; it too was rolled back. A fresh query returned nurse visit 1 with status `booked`, confirming both attempted changes were undone. See the observed sequence in `../evidence/portfolio-3/row-lock-observation.md` and the final result in `../evidence/portfolio-3/lock-final-state.csv`.

This is evidence of PostgreSQL's row-level write conflict behavior in the tested session. It is not a benchmark or a claim about production throughput. A screenshot of the final query result is saved at `../evidence/portfolio-3/pgadmin-lock-final-state.jpg` and uploaded to GitHub.


