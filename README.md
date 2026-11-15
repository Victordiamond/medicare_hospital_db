# MIT 8103 Advanced Database Systems — MediCare

**Case study:** MediCare Hospital Management System, developed here as a simulated telemedicine platform.  
**GitHub repository:** https://github.com/Victordiamond/medicare_hospital_301911811

Patients search for doctors, book a video consultation, share symptoms, and receive a prescription. They can locate nearby pharmacies to fulfil it or select a nurse and schedule prescription-linked care visits over a planned treatment period. Doctors, nurses, pharmacy staff, and billing staff have separate database responsibilities.

All sample identities, contact information, clinical details, prescription values, and pharmacy points are fictional coursework data. Nothing in the examples is medical advice. The database stores a meeting reference; it does not implement an actual video service. Pharmacy distance is computed from a position supplied for a search; client map directions and routing are outside the database.

## Portfolio folders

1. [`portfolio-1-database-design/`](portfolio-1-database-design/) — case study, relational schema, ER diagram, constraints, and normalisation.
2. [`portfolio-2-query-optimisation/`](portfolio-2-query-optimisation/) — useful reads, indexes, and `EXPLAIN ANALYZE` comparison.
3. [`portfolio-3-transactions-concurrency/`](portfolio-3-transactions-concurrency/) — commit, rollback, savepoint, and two-session row-lock exercise.
4. [`portfolio-4-nosql/`](portfolio-4-nosql/) — MongoDB model, GeoJSON pharmacy search, nurse care requests, and indexes.
5. [`portfolio-5-distributed-cloud/`](portfolio-5-distributed-cloud/) — replication, availability, consistency, and partitioning/sharding design.

The 2–3 page LMS summary draft is in [`final-documentation/`](final-documentation/). Evidence requirements and current verification state are in [`evidence/CHECKLIST.md`](evidence/CHECKLIST.md). Evidence must be actual outputs/screenshots from your own local run; no screenshot or timing is represented as captured until saved in this repo.

## Run order

1. In pgAdmin, connect to `medicare_hospital_db` and run `portfolio-1-database-design/schema.sql`; it extends the existing tables without dropping them.
2. Review the report, pharmacy-distance, and nurse-schedule outputs at the end of that script.
3. Run the query plan exercise in Portfolio 2 and save both actual plans.
4. Run the safe transaction script in Portfolio 3. Use two query sessions for the row-lock section; roll back the second session's update.
5. In Compass, import the five JSON files in Portfolio 4 into collections named `patients`, `doctors`, `pharmacies`, `nurses`, and `nurseCareRequests`. Run `indexes.js`, then capture the nearby-pharmacy and nurse schedule query outputs.
6. Review the distributed design in Portfolio 5 and be ready to explain the availability/consistency trade-off.

Each major design decision is described in simple language in the portfolio README files. Add your measured results, screenshots, references, authentic personal reflection, and an accurate AI-use declaration before LMS submission. Current verification gaps are listed in `evidence/CHECKLIST.md`. LMS submission has not occurred.

