# MIT 8103 Advanced Database Systems — MediCare

**Case study:** MediCare Hospital Management System, developed here as a simulated telemedicine platform.  
**GitHub repository:** [MediCare portfolio on GitHub](https://github.com/Victordiamond/medicare_hospital_301911811)

Patients search for doctors, book a video consultation, share symptoms, and receive a prescription. They can locate nearby pharmacies to fulfil it or select a nurse and schedule prescription-linked care visits over a planned treatment period. Doctors, nurses, pharmacy staff, and billing staff have separate database responsibilities.

All sample identities, contact information, clinical details, prescription values, and pharmacy points are fictional coursework data. Nothing in the examples is medical advice. The database stores a meeting reference; it does not implement an actual video service. Pharmacy distance is computed from a position supplied for a search; client map directions and routing are outside the database.

## Portfolio folders

1. [`portfolio-1-database-design/`](portfolio-1-database-design/) — case study, relational schema, ER diagram, constraints, and normalisation.
2. [`portfolio-2-query-optimisation/`](portfolio-2-query-optimisation/) — useful reads, indexes, and `EXPLAIN ANALYZE` comparison.
3. [`portfolio-3-transactions-concurrency/`](portfolio-3-transactions-concurrency/) — commit, rollback, savepoint, and two-session row-lock exercise.
4. [`portfolio-4-nosql/`](portfolio-4-nosql/) — MongoDB model, GeoJSON pharmacy search, nurse care requests, and indexes.
5. [`portfolio-5-distributed-cloud/`](portfolio-5-distributed-cloud/) — replication, availability, consistency, and partitioning/sharding design.

The 2–3 page portfolio summary is in [`final-documentation/portfolio-summary.md`](final-documentation/portfolio-summary.md), with an editable Word copy alongside it. Evidence requirements and current verification state are in [`evidence/CHECKLIST.md`](evidence/CHECKLIST.md). Evidence entries distinguish captured results from work still outstanding.

## Run order

1. The Portfolio 1 schema and consultation report have been run in pgAdmin. The saved sample consultation symptom fields are blank, and pharmacy-distance and nurse-schedule outputs still need capture.
2. Portfolio 2 includes captured baseline and post-index plans for a two-appointment sample. PostgreSQL chose sequential scans in both; these results do not establish an index speedup.
3. Portfolio 3 includes a saved transaction result, two-session lock observation, final state, and one pgAdmin screenshot. Review the script before rerunning because it is an instructional two-session exercise.
4. Portfolio 4 was imported and queried in Compass. The geospatial explain screenshot is saved; focused document and nurse-result screenshots remain outstanding.
5. Portfolio 5 is a written architecture proposal only; no cloud deployment, failover, replica-lag, or restore test was performed.

The portfolio summary identifies the student and records an accurate AI-use statement and evidence-based reflection. Current verification gaps are listed in `evidence/CHECKLIST.md`. LMS submission has not occurred. The assessment brief asks for a private repository; this repository remains public by the student's instruction.

