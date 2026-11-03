-- Run in one pgAdmin Query Tool session. All data is temporary and fictional.
-- COMMIT demonstration: savepoint removes the second row; the first persists
-- for this session because the temporary table uses ON COMMIT PRESERVE ROWS.
BEGIN ISOLATION LEVEL READ COMMITTED;
CREATE TEMP TABLE IF NOT EXISTS transaction_demo (
    event_id integer PRIMARY KEY,
    note text NOT NULL
) ON COMMIT PRESERVE ROWS;
TRUNCATE pg_temp.transaction_demo;
INSERT INTO transaction_demo VALUES (1, 'committed example');
SAVEPOINT before_optional_event;
INSERT INTO transaction_demo VALUES (2, 'rolled back to savepoint');
ROLLBACK TO SAVEPOINT before_optional_event;
COMMIT;
SELECT * FROM transaction_demo ORDER BY event_id;

-- Full ROLLBACK demonstration: event 3 is undone and must not appear below.
BEGIN;
INSERT INTO transaction_demo VALUES (3, 'fully rolled back example');
ROLLBACK;
SELECT * FROM transaction_demo ORDER BY event_id;

-- Concurrency exercise (use two pgAdmin Query Tool sessions, same database):
-- Session A: BEGIN; SELECT nurse_visit_id, status FROM nurse_visits
--            WHERE nurse_visit_id = 1 FOR UPDATE;
-- Session B: BEGIN; UPDATE nurse_visits SET status='in_progress'
--            WHERE nurse_visit_id = 1;
-- Observe B waiting for A's row lock. Then COMMIT in A; B continues.
-- Then ROLLBACK in B to leave the demo booking unchanged (or COMMIT it).
-- Under READ COMMITTED, B sees the committed row version after the wait.
-- Use a separate billing_id in two sessions to show independent row updates.

