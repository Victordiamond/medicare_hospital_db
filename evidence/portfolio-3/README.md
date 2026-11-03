Verified in pgAdmin on 2026-11-03: the temporary transaction demo completed, and a follow-up query returned only the single committed row after the savepoint and full rollback. CSV is in `transaction-final-state.csv`.

Screenshot and the separate two-session row lock waiting/release exercise are still pending. Roll back Session B after observing the lock.

