# Portfolio 4 — NoSQL and advanced data models

MongoDB Compass implementation uses the same MediCare telemedicine scenario. `patients` documents embed video consultation subdocuments with symptom summary, doctor reference, medical record, prescription, pharmacy fulfillment state, bill, and payment details. Separate `doctors`, `pharmacies`, and `nurses` collections hold profiles. Pharmacy GeoJSON coordinates support a `2dsphere` proximity index. `nurseCareRequests` stores the patient, prescription, selected nurse, treatment date range/frequency, and multiple scheduled care visits in one request document.

This model makes a patient-centered consultation history read in one document fetch and keeps a nurse request with its repeated visit schedule. Embedding is suitable while arrays stay bounded and the items are usually read with the parent. Separate doctor, nurse, and pharmacy documents avoid repeating profile fields. The trade-off is that cross-patient reporting, global billing summaries, and changes to embedded visit content can be harder than in normalized SQL. Referential consistency across patient, doctor, nurse, pharmacy, and prescription identifiers is application-managed.

Import [`patients.json`](patients.json), [`doctors.json`](doctors.json), [`pharmacies.json`](pharmacies.json), [`nurses.json`](nurses.json), and [`nurse_care_requests.json`](nurse_care_requests.json) into collections with matching names (use `nurseCareRequests` for the last). Create the indexes in [`indexes.js`](indexes.js), then run the examples in [`queries.mongodb.js`](queries.mongodb.js). The local database was previously verified in Compass with two patient documents and two doctor documents; the new collections and indexes have not yet been verified there.

All profiles and location points in these files are fictional coursework data. Sample medication text and instructions are placeholders, not care recommendations.

