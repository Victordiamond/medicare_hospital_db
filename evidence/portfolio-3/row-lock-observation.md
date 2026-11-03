# PostgreSQL row-lock observation — 2026-11-03

Database: `medicare_hospital_db` in pgAdmin 4. Row: `nurse_visits.nurse_visit_id = 1`.

1. Session A ran `BEGIN; SELECT nurse_visit_id, status FROM nurse_visits WHERE nurse_visit_id = 1 FOR UPDATE;` and returned row 1 with status `booked`. A remained in a transaction and held the row lock.
2. Session B ran `BEGIN; UPDATE nurse_visits SET status='in_progress' WHERE nurse_visit_id=1;`. pgAdmin showed the query was in progress and waiting while A held its lock.
3. Session A ran `COMMIT;` successfully (pgAdmin reported 148 ms). Session B then completed `UPDATE 1` after about 26 seconds total.
4. Session B ran `ROLLBACK;` successfully (123 ms), so its status change was not retained.
5. An additional query tool had accidentally queued the same update. That transaction also completed after A released the lock and was rolled back (110 ms).
6. A fresh query returned exactly `1, booked` (one row; query completed in 243 ms). The exported result is `lock-final-state.csv`.

Conclusion: the second transaction waited on the row-level lock and continued after the first transaction committed. Both attempted changes were rolled back; the final sample row remained unchanged. The extra queued session is disclosed here rather than omitted. This evidence supports the observed behavior in this local test only.
