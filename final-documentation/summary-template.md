# MIT 8103 Advanced Database Systems — Practical Portfolio

**Student:** [enter your name and matriculation number]  
**Session:** 2026/2027, First Semester  
**Case study:** MediCare telemedicine platform (simulated)  
**GitHub repository:** https://github.com/Victordiamond/medicare_hospital_301911811

## Case study and portfolio 1 — relational design

MediCare is a simulated telemedicine platform used by patients, doctors, nurses, and pharmacy staff. Patients find a doctor and book a video consultation, share symptoms, and receive a prescription. They can locate nearby pharmacies or request a nurse for prescription-linked care with a planned schedule of visits. PostgreSQL tables cover patients, doctors, consultations, records, prescriptions, pharmacy fulfillment, nurses, care requests, visits, billing, and payments. Foreign keys, uniqueness rules, and check constraints protect important relationships and values. The sample data are fictional.

The schema and two-row consultation report ran in pgAdmin. The report shows the fictional appointments, but both seeded `symptoms_summary` values are blank, so the current output does not demonstrate symptom capture. The pharmacy-distance and nurse-schedule SELECT statements exist in the schema script; their result outputs have not been saved as evidence.

**Student's design explanation:** [In your own words, explain the appointment relationships, one integrity rule, and one normalisation decision.]

## Portfolio 2 — query processing and optimisation

The SQL file includes a patient-history report joining patients, appointments, doctors, and optional medical records. Its measured plan comparison is a separate appointment lookup filtered by patient and sorted by appointment time, plus a completed-payment aggregation.

**Measured result (PostgreSQL 18, two appointment rows):** Before the composite index, PostgreSQL used `Seq Scan` followed by `Sort`; estimated and actual rows were 1, shared buffers were hit=3, and execution time was 0.068 ms. After index creation it still used `Seq Scan` and `Sort`; shared buffers were hit=3 and execution time was 0.087 ms. The patient email subquery used its existing unique index in both plans. The completed-payment aggregation was also run; it used a sequential scan of one payment row and a hash aggregate, took 0.091 ms, and did not use the partial index. These tiny measurements do not show an index speedup. Raw CSV plans are in `evidence/portfolio-2/`.

## Portfolio 3 — transactions and concurrency

The transaction script demonstrates `COMMIT`, `ROLLBACK`, and savepoint rollback on a temporary table so the hospital demo rows are not changed. A two-session exercise uses `SELECT ... FOR UPDATE` to show how PostgreSQL waits when two sessions update the same nurse-visit row.

**Observed result:** The pgAdmin transaction demo committed event 1, rolled event 2 back to a savepoint, and fully rolled event 3 back. The follow-up query returned only `1, committed example`. In the two-session test, Session B waited about 26 seconds for Session A to release nurse visit 1; both attempted changes were rolled back and the final row remained `booked`. CSVs, the observed sequence, and the final-query screenshot are in `evidence/portfolio-3/`; the screenshot is uploaded to GitHub.

## Portfolio 4 — NoSQL and advanced data models

MongoDB Compass shows 2 patients, 2 doctors, 2 pharmacies, 2 nurses, and 1 nurse care request with two booked visits. Six secondary indexes were verified. The nearby-pharmacy query returned Yaba then Ikeja; the patient timeline returned Ada's video consultation; the nurse aggregation returned both scheduled visits and linked prescription DEMO-RX-001. The geospatial plan used `location_2dsphere` (`GEO_NEAR_2DSPHERE`), examined 4 keys and 4 documents, returned 2, and reported 9 ms on the two-pharmacy sample. The existing Compass patient document initially lacked `prescriptionId`; one fictional record was updated and the rerun succeeded. The Compass connection and geospatial plan screenshot is uploaded to GitHub. Focused screenshots of the documents and nurse output remain pending. These counts and timings describe demo data only.

## Portfolio 5 — distributed/cloud exercise

The design discussion proposes a PostgreSQL primary, standby, read replica, and MongoDB replica set, with a single authoritative writer for correctness-sensitive bookings and payments. It explains replica lag, failover fencing, backups, and why partitioning or sharding should follow measured need. It is a design exercise only: no cloud deployment, failover, lag measurement, or restore drill was performed.

## Technical reflection — write this yourself

[Describe one real problem you encountered, how you diagnosed/fixed it, a design decision you would change after testing, and what you learned. Use your actual work and evidence; do not use a generated personal story.]

## AI use and references

**AI-use declaration (complete truthfully):** “I used ChatGPT to [state what help it provided, for example: organise requirements, explain design options, draft example SQL]. I personally [state exactly what you reviewed, ran, tested, corrected, and wrote yourself]. I verified the submitted results by [name the actual evidence].” Add any other tools, datasets, libraries, and documentation you used. Do not claim a test, review, or reflection you did not perform.

**References:** [List the PostgreSQL and MongoDB documentation, course materials, datasets, diagrams, and other sources actually consulted, using the citation style required by your lecturer.]


