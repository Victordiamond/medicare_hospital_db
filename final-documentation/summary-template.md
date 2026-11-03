# MIT 8103 Advanced Database Systems — Practical Portfolio

**Student:** [enter your name and matriculation number]  
**Session:** 2026/2027, First Semester  
**Case study:** MediCare telemedicine platform (simulated)  
**GitHub repository:** https://github.com/Victordiamond/medicare_hospital_db

## Case study and portfolio 1 — relational design

MediCare is a simulated telemedicine platform used by patients, doctors, nurses, and pharmacy staff. Patients find a doctor and book a video consultation, share symptoms, and receive a prescription. They can locate nearby pharmacies or request a nurse for prescription-linked care with a planned schedule of visits. PostgreSQL tables cover patients, doctors, consultations, records, prescriptions, pharmacy fulfillment, nurses, care requests, visits, billing, and payments. Foreign keys, uniqueness rules, and check constraints protect important relationships and values. The sample data are fictional.

**Student's design explanation:** [In your own words, explain the appointment relationships, one integrity rule, and one normalisation decision.]

## Portfolio 2 — query processing and optimisation

The consultation-history query joins patients, video appointments, doctors, and optional medical records. The optimisation exercise captures PostgreSQL's `EXPLAIN (ANALYZE, BUFFERS)` output before and after a composite patient/date index, and examines a partial index for completed payments.

**Measured result:** [Paste the actual plan/timings from your pgAdmin run. State row counts, plan nodes, buffers, and whether the index was chosen. The demo is tiny, so a sequential scan may be the right plan. Do not claim an improvement unless your captured output shows it.]

## Portfolio 3 — transactions and concurrency

The transaction script demonstrates `COMMIT`, `ROLLBACK`, and savepoint rollback on a temporary table so the hospital demo rows are not changed. A two-session exercise uses `SELECT ... FOR UPDATE` to show how PostgreSQL waits when two sessions update the same billing row.

**Observed result:** [Record what appeared in each session and how commit/rollback affected it. Add screenshots or query output.]

## Portfolio 4 — NoSQL and advanced data models

MongoDB embeds video consultation history and prescription details in patient documents; separate doctor, nurse, and pharmacy collections support shared profiles and pharmacy geospatial search. Nurse care requests reference the prescription and nurse and embed repeated visit slots. This suits patient-centered reads but trades off relationally enforced references. Compass evidence should show the imported fictional collections, indexes, and search results.

## Portfolio 5 — distributed/cloud exercise

The design discussion proposes a PostgreSQL primary with a standby replica, read-only search/reporting replicas, tested failover and backups, and carefully chosen partitioning/sharding only if multi-region scale requires it. Replication lag and cross-shard operations affect consistency. This is a design exercise; no cloud deployment is claimed.

## Technical reflection — write this yourself

[Describe one real problem you encountered, how you diagnosed/fixed it, a design decision you would change after testing, and what you learned. Use your actual work and evidence; do not use a generated personal story.]

## AI use and references

**AI-use declaration (complete truthfully):** “I used ChatGPT to [state what help it provided, for example: organise requirements, explain design options, draft example SQL]. I personally [state exactly what you reviewed, ran, tested, corrected, and wrote yourself]. I verified the submitted results by [name the actual evidence].” Add any other tools, datasets, libraries, and documentation you used. Do not claim a test, review, or reflection you did not perform.

**References:** [List the PostgreSQL and MongoDB documentation, course materials, datasets, diagrams, and other sources actually consulted, using the citation style required by your lecturer.]

