# CA evidence checklist

The local database work and document model were confirmed in an earlier pgAdmin/Compass session; status below distinguishes that from evidence still to capture for the portfolio.

| Requirement | Current status | Action for final portfolio |
| --- | --- | --- |
| Case study stated consistently | Drafted as a telemedicine platform | Confirm users and scope match your project, and explain the patient-to-doctor-to-prescription flow. |
| PostgreSQL telemedicine schema and sample report | Earlier seven-table model was verified; telemedicine migration has not yet run | Run the updated SQL; capture consultation, pharmacy-distance, and nurse-schedule outputs. |
| ERD and normalisation explanation | Drafted | Review relationships and defend the normalization choices. |
| Query plans and performance analysis | Script prepared, results not yet recorded | Run `portfolio-2-query-optimisation/queries.sql`; paste actual plans and explain observed outcomes. |
| Commit, rollback, savepoint | Script prepared, results not yet recorded | Run `portfolio-3-transactions-concurrency/transactions.sql`; capture output. |
| Concurrent row lock | Exercise documented, not yet observed | Use two pgAdmin sessions; record the wait/release and final row state. |
| MongoDB model | Patient/doctor collections previously verified; new pharmacy/nurse collections are prepared only | Import the new JSON collections, build the indexes, and capture a nearby-pharmacy search and nurse schedule. |
| Distributed/cloud activity | Design discussion drafted; no cloud setup claimed | Add an architecture sketch and explain availability/consistency trade-offs in your own words. |
| GitHub repository and progressive commits | Private repository created; portfolio draft committed and folder paths verified | Add actual evidence and later updates as you complete them. Do not claim this represents development throughout the semester or fabricate earlier history. |
| 2–3 page LMS documentation | Draft template only | Fill measurements, references, actual GitHub URL, and your own reflection; check final page count. |
| AI declaration and source acknowledgement | Suggested declaration included | Make it accurate to the assistance and review you actually performed. |
| LMS submission | Not performed | Submit the finished documentation and evidence yourself after review. |

All demo clinical data and pharmacy points are fictional and placeholder-only. Keep real patient information and precise user locations out of coursework screenshots and repository files.

