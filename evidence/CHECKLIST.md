# CA evidence checklist

This table records what was actually run locally on 3 November 2026. Keep the screenshots in the evidence folders when captured; do not treat drafted scripts or diagrams as test results.

| Requirement | Verified status | Next step |
| --- | --- | --- |
| Case study | Draft consistently describes MediCare as telemedicine: video consultation, clinician prescription, pharmacy search, nurse follow-up bookings. | Review wording and defend scope. |
| PostgreSQL schema | `medicare_hospital_db` is connected in pgAdmin. The schema script ran successfully in pgAdmin; its messages are saved in `portfolio-1/postgresql-schema-run.txt`. | Capture screenshot. Re-run report with richer non-NULL demo symptoms/diagnoses if appropriate; save outputs for nurse schedule and pharmacy proximity. |
| Consultation report | Actual two-row CSV saved in `portfolio-1/consultation-report.csv`. | Capture pgAdmin screenshot and explain the sample data. |
| ERD and normalization | Drafted; not independently reviewed by student. | Review relationships and explain normalization. |
| Query plans | Both baseline and post-index `EXPLAIN ANALYZE` plans saved as CSV. Both chose Seq Scan on the two-row appointments table. | Capture screenshot; run query suite/partial payment index; explain tiny-sample limitation. |
| Commit/rollback/savepoint | Transaction script ran; follow-up query showed exactly event 1 (`committed example`) after savepoint and full rollback. CSV saved in `portfolio-3/transaction-final-state.csv`. | Capture screenshot. |
| Concurrent row lock | Documented but not yet observed in two sessions. | Perform in two sessions, record wait and release, then rollback B. |
| MongoDB documents | Compass shows 2 patients, 2 doctors, 2 pharmacies, 2 nurses, and 1 nurse care request with 2 care visits. | Capture screenshots. |
| Mongo indexes and queries | Only automatic `_id` indexes are confirmed; additional indexes and sample queries have not yet been run. | Create indexes; execute near-pharmacy, consultation, and nurse schedule queries; save evidence. |
| Distributed/cloud activity | Architecture discussion and diagram drafted. No cloud deployment claimed. | Review and defend consistency, failover and scale-out choices. |
| GitHub | Private repository contains the portfolio drafts; actual outputs from this session still need uploading. | Upload evidence and later updates. Do not claim semester-long progressive history. |
| LMS summary and AI declaration | Template only; student reflection and declaration require truthful personal completion. | Complete and page-check the final 2–3 page document. |
| LMS submission | Not performed. | Student reviews and submits. |

All records and pharmacy points are fictional coursework examples. Sample medication text is not medical guidance.

