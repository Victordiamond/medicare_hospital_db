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

**Measured result (PostgreSQL 18, two appointment rows):** Both EXPLAIN ANALYZE plans estimated one result row and returned one. Before the composite index, the appointment access used `Seq Scan` followed by `Sort`; shared buffers were hit=3 and execution time was 0.068 ms. After index creation, PostgreSQL still chose `Seq Scan` and `Sort`; shared buffers were hit=3 and execution time was 0.087 ms. The patient-email lookup used its existing unique index in both runs. These tiny times do not establish a performance change; a larger dataset is needed. Raw outputs: `evidence/portfolio-2/plan-before-index.csv` and `plan-after-index.csv`. The completed-payment partial-index query is not yet tested.

## Portfolio 3 — transactions and concurrency

The transaction script demonstrates `COMMIT`, `ROLLBACK`, and savepoint rollback on a temporary table so the hospital demo rows are not changed. A two-session exercise uses `SELECT ... FOR UPDATE` to show how PostgreSQL waits when two sessions update the same nurse-visit row.

**Observed result:** The pgAdmin transaction demo committed event 1, rolled the optional event 2 back to a savepoint, then fully rolled event 3 back. A follow-up query returned only `1, committed example`; CSV: `evidence/portfolio-3/transaction-final-state.csv`. The two-session row-lock waiting/release exercise and screenshots are still pending.

## Portfolio 4 — NoSQL and advanced data models

MongoDB Compass shows 2 patient, 2 doctor, 2 pharmacy and 2 nurse documents plus 1 nurse care request containing two scheduled visits. Patient documents embed video consultation history and prescriptions; separate profile collections avoid repeated clinician and pharmacy fields. Pharmacy documents contain GeoJSON points. Six secondary indexes were created and verified. The nearest-pharmacy query returned two pharmacies; the patient timeline returned Ada’s video consultation; the nurse aggregation returned two booked visits and clinician prescription DEMO-RX-001. The geospatial plan used `location_2dsphere` (`GEO_NEAR_2DSPHERE`), examined 4 keys and 4 documents, returned 2, and reported 9 ms on the two-pharmacy sample. The imported patient was missing the embedded prescriptionId; an updateOne matched and modified one demo record, after which the aggregation succeeded. Screenshot files remain pending.

## Portfolio 5 — distributed/cloud exercise

The design discussion proposes a PostgreSQL primary with a standby replica, read-only search/reporting replicas, tested failover and backups, and carefully chosen partitioning/sharding only if multi-region scale requires it. Replication lag and cross-shard operations affect consistency. This is a design exercise; no cloud deployment is claimed.

## Technical reflection — write this yourself

[Describe one real problem you encountered, how you diagnosed/fixed it, a design decision you would change after testing, and what you learned. Use your actual work and evidence; do not use a generated personal story.]

## AI use and references

**AI-use declaration (complete truthfully):** “I used ChatGPT to [state what help it provided, for example: organise requirements, explain design options, draft example SQL]. I personally [state exactly what you reviewed, ran, tested, corrected, and wrote yourself]. I verified the submitted results by [name the actual evidence].” Add any other tools, datasets, libraries, and documentation you used. Do not claim a test, review, or reflection you did not perform.

**References:** [List the PostgreSQL and MongoDB documentation, course materials, datasets, diagrams, and other sources actually consulted, using the citation style required by your lecturer.]


