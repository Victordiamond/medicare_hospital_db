# Portfolio 4 — NoSQL and advanced data models

## Case study and model

MediCare is the same fictional telemedicine service used in Portfolios 1–3 and 5. Patients book video consultations, doctors add clinical notes and prescriptions, patients search for nearby pharmacies, and nurses schedule follow-up visits linked to a clinician's prescription.

This portfolio implements a **document model in MongoDB**. A patient's consultation history, clinical note, prescription, and billing summary are embedded inside the patient document because these details are commonly read together for one patient's timeline. Doctor, nurse, and pharmacy profiles remain separate collections so their details are not copied into every patient record. A nurse-care request is also a separate document; it references a patient, nurse, and prescription by stable IDs and embeds its bounded list of planned visits.

Pharmacies store GeoJSON points. A `2dsphere` index lets MongoDB find nearby active pharmacies in distance order. The sample coordinate and pharmacy locations are fictional coursework data, not a live navigation service.

## Why this model fits, and its trade-offs

- Embedding makes a patient's history and billing summary available in one document read and keeps related history together.
- References avoid duplicating reusable doctor, nurse, and pharmacy profiles. The nurse schedule aggregation joins a care request to the referenced patient document to check the prescription ID.
- The visit array is appropriate for this small bounded schedule. If a patient accumulates a very large or unbounded visit history, visits should move to a separate collection.
- MongoDB does not enforce the cross-document patient/nurse/prescription references as relational foreign keys do. The application must validate that these IDs exist and that a nurse visit references the intended clinician prescription.
- The embedded billing copy is useful for a patient-history read, but payment reconciliation should use the PostgreSQL billing/payment records as the authoritative ledger in this hybrid design.

## Implementation and evidence

The seed documents are `patients.json`, `doctors.json`, `pharmacies.json`, `nurses.json`, and `nurse_care_requests.json`. `indexes.js` creates indexes for video-capable doctor discovery, appointment history, pharmacy geospatial search, active nurses by specialty, and patient/nurse care-request schedules. `queries.mongodb.js` contains the pharmacy search, consultation-history query, and nurse schedule aggregation.

MongoDB Compass was connected to `localhost:27017/medicare_hospital_db` on 3 November 2026. It showed 2 patients, 2 doctors, 2 pharmacies, 2 nurses, and 1 nurse care request. The indexed pharmacy query returned Yaba then Ikeja within 10 km. The schedule aggregation returned the care request with two booked visits and its linked clinician prescription. The `explain("executionStats")` plan used `location_2dsphere`, examined 4 keys and 4 documents, returned 2 pharmacies, and reported 9 ms. This tiny two-pharmacy sample demonstrates index selection; it does not establish production performance.

The already-imported local patient document initially lacked the nested `prescriptionId`, so the first schedule aggregation returned an empty array. A Compass `updateOne` matched and modified one fictional record to add the ID; the rerun returned the linked schedule. The checked-in `patients.json` seed already includes it. This difference between the imported state and the seed is documented in [`../evidence/portfolio-4/import-verification.md`](../evidence/portfolio-4/import-verification.md).

Observed results and the explain summary are in [`../evidence/portfolio-4/mongodb-execution.txt`](../evidence/portfolio-4/mongodb-execution.txt). A Compass shell screenshot is saved locally at [`../evidence/portfolio-4/compass-shell-results.jpg`](../evidence/portfolio-4/compass-shell-results.jpg); it still needs upload to GitHub. All sample data are fictional, and medication placeholders are not medical advice.

## How to reproduce

1. Connect Compass to `mongodb://localhost:27017`.
2. Import the five JSON files into `medicare_hospital_db` using their matching collection names.
3. Run `indexes.js` in mongosh to create the secondary indexes.
4. Run each query in `queries.mongodb.js`; use the sample coordinate as a demo search origin.
5. Run the geospatial query with `explain("executionStats")` and compare the returned stage and counts with the observed plan evidence.

When reusing a database with earlier sample imports, verify that Ada's embedded prescription contains `prescriptionId: "DEMO-RX-001"` before running the nurse aggregation.

