# Query plan results — measured in pgAdmin

PostgreSQL 18.0 on this local demo database; two appointment rows. The raw `EXPLAIN (ANALYZE, BUFFERS, VERBOSE)` CSV captures are in `../evidence/portfolio-2/plan-before-index.csv` and `plan-after-index.csv`.

| Run | Appointment access plan | Estimated rows | Actual rows | Buffers | Execution time |
| --- | --- | ---: | ---: | --- | ---: |
| Before composite index | Seq Scan; Sort | 1 | 1 | shared hit=3 | 0.068 ms |
| After composite index | Seq Scan; Sort | 1 | 1 | shared hit=3 | 0.087 ms |

The `patients` email lookup used its existing unique index in both plans. PostgreSQL did not use the new appointment index; for only two appointment rows, reading the table directly costs less than consulting an index and then visiting table pages. The measured time difference is tiny and should not be treated as a performance regression or improvement. A larger realistic dataset is needed for a meaningful benchmark.

The covering appointment index was created and remains present: `(patient_id, appointment_start DESC) INCLUDE (status)`. The index did not change this query's chosen plan at the current scale.

## Completed payments aggregation

The partial index `idx_payments_completed_billing` on `payments (billing_id) INCLUDE (amount) WHERE status = 'completed'` was created in pgAdmin and the aggregation was run with `EXPLAIN (ANALYZE, BUFFERS, VERBOSE)`. The saved actual output is `../evidence/portfolio-2/completed-payment-plan.csv`.

At this data size the plan used a sequential scan of one matching payment row and a hash aggregate. Execution time was 0.091 ms, with one shared buffer hit during execution. The index was not selected. This is expected for a tiny table and does not demonstrate an index speedup; use larger data and repeat measurements before making such a claim.
