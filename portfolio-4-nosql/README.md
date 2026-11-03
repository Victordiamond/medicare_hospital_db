# Portfolio 4 — NoSQL and advanced data models

MongoDB Compass connected to `localhost:27017/medicare_hospital_db`. On 3 November 2026 the following fictional JSON collections were imported and visually verified: 2 patients, 2 doctors, 2 pharmacies, 2 nurses and 1 nurse care request. The request references a sample patient, nurse and prescription and embeds two scheduled visits. Pharmacy documents contain GeoJSON points.

The files are the seed data for a patient-centered consultation history, separate clinician/pharmacy/nurse profiles, and a nurse care request with a bounded visit schedule. Embedding makes these related timeline details convenient to retrieve with the patient or request; separate profile documents avoid repeating names and contact fields. The trade-off is that global reporting and referential integrity need additional queries/application checks.

Additional indexes and sample queries in `indexes.js` and `queries.mongodb.js` remain unexecuted; only the automatic `_id` indexes are currently verified. In particular, nearest-pharmacy `$near` needs the `location: 2dsphere` index before it can be tested. Capture Compass screenshots and query results after those steps.

All profiles, coordinates and care details are fictional. Medication instructions are placeholders, not health advice.

