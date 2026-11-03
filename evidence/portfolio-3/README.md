Verified in pgAdmin on 2026-11-03:

- The temporary transaction demo completed; a follow-up query returned the single committed row after the savepoint and full rollback. CSV: `transaction-final-state.csv`.
- The two-session row lock test completed. Session A locked nurse visit 1 using `SELECT ... FOR UPDATE`. Session B's update waited about 26 seconds, then completed after A committed. B was rolled back. A third query tool also queued the same update unintentionally; that update was also rolled back. A final SELECT returned `1, booked`, confirming no sample data change remained. CSV: `lock-final-state.csv`; observed sequence: `row-lock-observation.md`.

The lock behavior is verified. A screenshot of the final pgAdmin query result is saved locally; the private-repository browser session currently returns GitHub 404, so screenshot upload remains pending.
