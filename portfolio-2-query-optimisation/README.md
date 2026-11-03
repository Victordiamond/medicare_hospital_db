# Portfolio 2 — Query processing and optimisation

Run [`queries.sql`](queries.sql) in pgAdmin and save the actual `EXPLAIN (ANALYZE, BUFFERS)` output or screenshots. The patient-history query filters by a unique patient email, joins appointment/doctor data, and optionally retrieves the medical record. The plan comparison adds a composite index on `(patient_id, appointment_start DESC)` and includes `status`, matching the filter, sort, and projected fields. A partial index supports completed-payment aggregation.

Interpret the plan PostgreSQL actually returns: compare node types, estimated versus actual rows, buffer hits/reads, and execution time. The current sample contains only two appointments and one payment, so a sequential scan may be faster and may be selected despite the index. That is a valid result; do not claim the index improved runtime unless measured output supports that claim. Indexes consume disk and add write cost. For a meaningful scale comparison, use a separately labelled synthetic dataset with enough rows and run `ANALYZE`; do not mix that benchmark with the verified two-row production-like demo.

## Evidence still to capture

- Query output for the history query.
- Baseline plan and plan after index creation, with machine-reported timings.
- A short student-written comparison using those observed values.

