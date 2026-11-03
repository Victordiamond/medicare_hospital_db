# CA evidence checklist

This table records what was actually run locally on 3 November 2026. Keep the screenshots in the evidence folders when captured; do not treat drafted scripts or diagrams as test results.

| Requirement | Verified status | Next step |
| --- | --- | --- |
| Case study | Draft consistently describes MediCare as telemedicine: video consultation, clinician prescription, pharmacy search, nurse follow-up bookings. | Review wording and defend scope. |
| PostgreSQL schema | `medicare_hospital_db` is connected in pgAdmin. The schema script ran successfully in pgAdmin; its messages are saved in `portfolio-1/postgresql-schema-run.txt`. | Capture screenshot. Re-run report with richer non-NULL demo symptoms/diagnoses if appropriate; save outputs for nurse schedule and pharmacy proximity. |
| Consultation report | Actual two-row CSV saved in `portfolio-1/consultation-report.csv`. | Capture pgAdmin screenshot and explain the sample data. |
| ERD and normalization | Drafted; not independently reviewed by student. | Review relationships and explain normalization. |
| Query plans | Baseline and post-index appointment plans and the completed-payment aggregation plan are saved as CSV. All selected sequential scans at this sample size; the payment aggregate took 0.091 ms. | Capture screenshots and explain tiny-sample limitation. |
| Commit/rollback/savepoint | Transaction script ran; follow-up query showed exactly event 1 (`committed example`) after savepoint and full rollback. CSV saved in `portfolio-3/transaction-final-state.csv`. | Capture screenshot. |
| Concurrent row lock | Observed in pgAdmin on 2026-11-03: Session B waited about 26 seconds for Session A to commit; B and an accidentally queued duplicate update were rolled back; a final SELECT verified row 1 remained `booked`. Transcript and final-state CSV saved. | Capture pgAdmin screenshot and upload the transcript and CSV to GitHub. |
| MongoDB documents | Compass shows 2 patients, 2 doctors, 2 pharmacies, 2 nurses, and 1 nurse care request with 2 care visits. | Capture screenshots. |
| Mongo indexes and queries | Compass confirmed six non-`_id` indexes, nearest-active-pharmacy results, a linked nurse schedule and a 2dsphere explain plan. Evidence text is in `portfolio-4/mongodb-execution.txt`. The linked nurse query required correcting one stale local demo patient record; the imported JSON seed already contains that ID. | Capture Compass screenshots. |
| Distributed/cloud activity | Architecture discussion and diagram drafted. No cloud deployment claimed. | Review and defend consistency, failover and scale-out choices. |
| GitHub | Private repository contains portfolio drafts and the existing SQL/Mongo outputs. The completed-payment plan is now uploaded; confirm all evidence and current documentation stay in sync. | Capture and upload screenshots; final repository consistency review. Do not claim semester-long progressive history. |
| LMS summary and AI declaration | Template only; student reflection and declaration require truthful personal completion. | Complete and page-check the final 2–3 page document. |
| LMS submission | Not performed. | Student reviews and submits. |

All records and pharmacy points are fictional coursework examples. Sample medication text is not medical guidance.
