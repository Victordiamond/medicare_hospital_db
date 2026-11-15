# CA evidence checklist

This table records what was actually run locally on 3 November 2026. Keep the screenshots in the evidence folders when captured; do not treat drafted scripts or diagrams as test results.

| Requirement | Verified status | Next step |
| --- | --- | --- |
| Case study | Draft consistently describes MediCare as telemedicine: video consultation, clinician prescription, pharmacy search, nurse follow-up bookings. | Review wording and defend scope. |
| PostgreSQL schema | `medicare_hospital_db` is connected in pgAdmin. The schema script ran successfully; messages are in `evidence/portfolio-1/postgresql-schema-run.txt`. | Capture screenshot. Decide whether non-empty fictional symptoms are needed; pharmacy-distance and nurse-schedule outputs are not saved yet. |
| Consultation report | Actual two-row CSV is in `evidence/portfolio-1/consultation-report.csv`; each `symptoms_summary` is blank in the seeded appointment rows. | Capture screenshot; if the brief expects symptom capture, update only fictional demo rows and rerun the report. |
| ERD and normalization | Drafted; not independently reviewed by student. | Review relationships and explain normalization. |
| Query plans | Baseline and post-index appointment plans and the completed-payment aggregation plan are saved as CSV. The planner chose sequential scans at this sample size; the payment aggregate took 0.091 ms. | Capture pgAdmin screenshots and a history-query output; explain the tiny-sample limitation. |
| Commit/rollback/savepoint | Transaction script ran; follow-up query showed exactly event 1 (`committed example`) after savepoint and full rollback. CSV is in `evidence/portfolio-3/transaction-final-state.csv`. | Capture screenshot if the rubric requires it; CSV output is present. |
| Concurrent row lock | Observed in pgAdmin on 2026-11-03: Session B waited about 26 seconds for Session A to commit; B and an accidentally queued duplicate update were rolled back; a final SELECT verified row 1 remained `booked`. Transcript, final-state CSV, and final query screenshot are saved locally; screenshot is uploaded to GitHub. | Keep the extra queued update disclosed and explain the observed result. |
| MongoDB documents | Compass shows 2 patients, 2 doctors, 2 pharmacies, 2 nurses, and 1 nurse care request with 2 care visits. Portfolio 4 explains the document model, embedding/reference choices, geospatial query, and trade-offs. The Compass connection and geospatial-plan screenshot is saved locally and uploaded to GitHub. | Capture focused screenshots of the documents and nurse aggregation. |
| Mongo indexes and queries | Compass confirmed six non-`_id` indexes, nearest-active-pharmacy results, a linked nurse schedule and a 2dsphere explain plan. Evidence text is in `portfolio-4/mongodb-execution.txt`. The linked nurse query required correcting one stale local demo patient record; the imported JSON seed already contains that ID. | Capture focused Compass screenshots of the documents and nurse aggregation, then upload the evidence to GitHub. |
| Distributed/cloud activity | Portfolio 5 now includes a rendered SVG architecture, editable Mermaid source, read/write routing table, replication trade-offs, failure analysis, and defense prompts. No cloud deployment or failover/restore test is claimed. | Student reviews and can explain the choices; live availability/lag evidence remains unavailable without a deployed replica setup. |
| GitHub | The repository contains all five portfolio folders, SQL/Mongo outputs, the Portfolio 3 lock screenshot, the Portfolio 4 Compass screenshot, and the Portfolio 5 architecture. | Upload remaining pgAdmin/Compass screenshots if captured; verify repository paths and documentation before submission. Do not claim semester-long progressive history. |
| LMS summary and AI declaration | Template only; student reflection and declaration require truthful personal completion. | Complete and page-check the final 2–3 page document. |
| LMS submission | Not performed. | Student reviews and submits. |

All records and pharmacy points are fictional coursework examples. Sample medication text is not medical guidance.






