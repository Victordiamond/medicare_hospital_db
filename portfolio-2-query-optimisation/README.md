# Portfolio 2 — Query processing and optimisation

Run [`queries.sql`](queries.sql) in pgAdmin. It contains a patient-history report joining patient, appointment, doctor, and optional medical-record data. The measured plan comparison is a separate, narrower appointment lookup: it filters appointments by the selected patient's ID and sorts by appointment time. The composite index on `(patient_id, appointment_start DESC) INCLUDE (status)` matches that lookup's filter, sort, and selected fields. A separate partial index is evaluated for completed-payment aggregation.

Interpret the plan PostgreSQL actually returns: compare node types, estimated versus actual rows, buffer hits/reads, and execution time. The current sample contains only two appointments and one payment, so a sequential scan may be faster and may be selected despite the index. That is a valid result; do not claim the index improved runtime unless measured output supports that claim. Indexes consume disk and add write cost. For a meaningful scale comparison, use a separately labelled synthetic dataset with enough rows and run `ANALYZE`; do not mix that benchmark with the verified two-row production-like demo.

## Evidence status

- Baseline and post-index plans and the completed-payment plan are saved under [`../evidence/portfolio-2/`](../evidence/portfolio-2/), with measured values interpreted in [`plan-results.md`](plan-results.md).
- The history query's result output and pgAdmin screenshots have not been saved yet.
- Add a student-written comparison after reviewing the actual CSV plans; state that the index was not selected on this tiny sample.

