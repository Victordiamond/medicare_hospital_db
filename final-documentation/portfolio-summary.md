# MIT 8103 Advanced Database Systems — MediCare portfolio

**Student:** Victor Ubah  
**Student number:** 301911811  
**Session:** 2026/2027 Academic Session, First Semester  
**GitHub repository:** [MediCare portfolio](https://github.com/Victordiamond/medicare_hospital_301911811)

## Project and portfolio 1 — relational design

MediCare is modelled as a simulated telemedicine platform. Patients find doctors, book video consultations, share symptoms, and receive prescriptions. They can search for nearby pharmacies or request prescription-linked nurse visits. PostgreSQL separates patients, doctors, appointments, medical records, prescriptions, pharmacy fulfillment, nurses, care requests, visits, billing, and payments. Foreign keys preserve valid relationships; uniqueness and check constraints protect identifiers, appointment slots, statuses, and values. Separate care-request and visit tables allow one treatment plan to contain multiple scheduled visits; separate billing and payment tables allow installment payments.

The schema and consultation report were run in pgAdmin and the report returned two fictional appointments. Both saved `symptoms_summary` values are blank, so the output does not demonstrate symptom capture. Pharmacy-distance and nurse-schedule result outputs are not saved yet.

## Portfolio 2 — query optimisation

The saved patient-history query is distinct from the measured appointment lookup. On the two-appointment sample, the lookup used a sequential scan and sort before and after the composite index: 0.068 ms before and 0.087 ms after, with three shared-buffer hits in each. The completed-payment aggregation scanned one row and took 0.091 ms; it did not use its partial index. These small measurements show no index speedup. The saved plans are in `evidence/portfolio-2/`.

## Portfolio 3 — transactions and concurrency

The temporary-table exercise demonstrated commit, savepoint rollback, and full rollback; the final result retained only the committed example. In the two-session row-lock exercise, Session B waited about 26 seconds while Session A held nurse visit 1. After the lock was released, B's update completed and was rolled back. The final row remained `booked`. CSV output, the observation record, and a pgAdmin screenshot are included in `evidence/portfolio-3/`.

## Portfolio 4 — MongoDB

Compass showed 2 patients, 2 doctors, 2 pharmacies, 2 nurses, and 1 nurse-care request with two booked visits. Six secondary indexes were confirmed. The nearby-pharmacy query returned Yaba then Ikeja; the nurse aggregation returned two visits linked to prescription `DEMO-RX-001`. The geospatial plan used `location_2dsphere`, examined four keys and four documents, returned two pharmacies, and reported 9 ms on this small sample. A seeded patient document lacked `prescriptionId`; ChatGPT corrected that fictional document and the nurse aggregation then returned the expected visits. The Compass connection/explain screenshot is included. Focused document and nurse-output screenshots remain outstanding.

## Portfolio 5 — distributed database design

The proposal uses PostgreSQL as the authoritative writer, with a standby, a read-only replica for stale-tolerant reads, and MongoDB for patient-history documents. It explains replica lag, failover fencing, backups, and when partitioning or sharding could be considered. This is a design proposal only; no cloud deployment, failover, replica-lag measurement, or restore drill was performed.

## Individual technical reflection

I defined MediCare as a telemedicine service with video consultations, pharmacy discovery, and prescription-linked nurse visits so the database work reflected the intended service. The saved MongoDB check exposed a patient document missing `prescriptionId`, which prevented the nurse aggregation from matching the prescription until ChatGPT corrected the fictional sample. This showed why an import should validate referenced identifiers across collections. I would add an automated import check for those references before accepting a dataset.

## AI use and references

**AI-use declaration:** ChatGPT was used to interpret the assessment requirements, shape the relational and document models, draft SQL, MongoDB queries and explanations, create documentation, operate the recorded pgAdmin and Compass checks, and correct the stale fictional MongoDB sample. Victor Ubah supplied the telemedicine requirements, chose the repository name, requested verification, and reviewed the package for missing fields. The saved database evidence records the assistant-operated checks; Victor has not independently rerun every database command. Sample records are fictional coursework data and are not clinical advice.

**References:** School of Post Graduate Studies, *MIT 8103 Advanced Database Systems: First Semester Continuous Assessment Brief*, 2026/2027. PostgreSQL, [Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html), [Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html), [Explicit Locking](https://www.postgresql.org/docs/18/explicit-locking.html), and [High Availability](https://www.postgresql.org/docs/18/high-availability.html). MongoDB, [Embedded Data](https://www.mongodb.com/docs/manual/data-modeling/embedding/), [Geospatial Queries](https://www.mongodb.com/docs/manual/geospatial-queries/), and [Replication](https://www.mongodb.com/docs/manual/replication/). ChatGPT assisted with this coursework package; these references were consulted during its preparation.

