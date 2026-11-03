# MongoDB Compass import observations (3 November 2026)

Connection shown in Compass: `localhost:27017`, database `medicare_hospital_db`.

| Collection | Documents visible in Compass | Key checked |
| --- | ---: | --- |
| `doctors` | 2 | Demo doctors Tunde Bello and Amara Eze |
| `patients` | 2 | Patient Ada's video visit, clinician record, prescription and payment fields are embedded |
| `pharmacies` | 2 | Demo Pharmacy Ikeja and Yaba; each displays GeoJSON `location` object |
| `nurses` | 2 | Demo nurses Kemi and Emeka |
| `nurseCareRequests` | 1 | `DEMO-CARE-001` references patient, prescription and nurse and embeds two visits |

Compass displayed import-success notices for the three added collections: 2 pharmacy documents, 2 nurse documents and 1 nurse care request. These are sample coursework records only.

Only Compass automatic `_id` indexes have been confirmed. The additional indexes and queries in the JS files have not been executed. A mongosh connection attempt from the restricted command environment was denied; use Compass or a permitted local session to create indexes and run queries. Screenshots are still to be captured.

