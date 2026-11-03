# MongoDB Compass import and query observations (3 November 2026)

Connection: `localhost:27017`, database `medicare_hospital_db`.

| Collection | Documents visible in Compass | Checked content |
| --- | ---: | --- |
| `doctors` | 2 | Tunde Bello and Amara Eze |
| `patients` | 2 | Ada's video visit, clinical sample, prescription and billing fields |
| `pharmacies` | 2 | Ikeja and Yaba sample pharmacies with GeoJSON points |
| `nurses` | 2 | Kemi and Emeka |
| `nurseCareRequests` | 1 | `DEMO-CARE-001` references patient, prescription and nurse; includes two booked visits |

Compass showed imports completed for 2 pharmacy documents, 2 nurse documents and 1 nurse care request. All rows are fictional.

The six secondary indexes, nearby-pharmacy query, patient timeline, nurse schedule aggregation and a geospatial `explain("executionStats")` were run in the Compass shell. The exact observed summaries are in [`mongodb-execution.txt`](mongodb-execution.txt). The geospatial query used `location_2dsphere`, returned both pharmacies, and examined four index keys and four documents in this two-record sample.

The preexisting patient document was imported before the nested prescriptionId was present. The first nurse aggregation returned no rows; a Compass `updateOne` matched and modified one fictional patient to add the id, and the rerun returned the expected linked nurse request. The checked-in `patients.json` seed already contains this field.

Screenshots of the Compass imports and query results remain to be saved to this folder.

