Verified in pgAdmin on 2026-11-03:

- The temporary transaction demo completed; a follow-up query returned the single committed row after the savepoint and full rollback. CSV: `transaction-final-state.csv`.
- The two-session row lock test completed. Session A locked nurse visit 1 using `SELECT ... FOR UPDATE`. Session B's update waited about 26 seconds, then completed after A committed. B was rolled back. A third query tool also queued the same update unintentionally; that update was also rolled back. A final SELECT returned `1, booked`, confirming no sample data change remained. CSV: `lock-final-state.csv`; observed sequence: `row-lock-observation.md`.

The lock behavior is verified. The actual pgAdmin final query screenshot is saved as `pgadmin-lock-final-state.jpg` and uploaded to the GitHub evidence folder. A screenshot of the temporary-table transaction query is not available; the transaction's final CSV output is included.


