# Portfolio 4 — NoSQL and advanced data models

MongoDB Compass is connected to `localhost:27017/medicare_hospital_db`. On 3 November 2026 Compass verified 2 patients, 2 doctors, 2 pharmacies, 2 nurses, and 1 nurse care request with two visit slots. The current dataset is fictional.

The shell created and verified these indexes: doctor specialization/video flag; patient appointment time; pharmacy GeoJSON `2dsphere`; nurse specialty/active status; and care-request patient/date and nurse/date. The `$near` search returned both sample pharmacies in nearest-first order. The consultation history returned Ada Nwosu’s video visit and prescription. The corrected nurse schedule aggregation returned `DEMO-CARE-001`, its two booked visits, and the linked clinician prescription. Raw observations and the MongoDB geospatial execution plan are in [`../evidence/portfolio-4/mongodb-execution.txt`](../evidence/portfolio-4/mongodb-execution.txt).

The imported Compass patient record came from an earlier seed that lacked the embedded `prescriptionId`; `updateOne` matched and modified one fictional record to add `DEMO-RX-001`, after which the nurse aggregation succeeded. The checked-in `patients.json` seed already includes that field.

Embedding consultation/prescription history suits patient-centered reads. Separate profiles prevent repeated contact information. Nurse requests keep a bounded set of visits together. The cost is that cross-document references need application checks. All medication values and locations are placeholders, not clinical advice. Screenshots remain to be saved in the repository.

