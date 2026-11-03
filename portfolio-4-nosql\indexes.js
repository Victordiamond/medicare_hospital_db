// Run in mongosh after importing the collections in medicare_hospital_db.
db = db.getSiblingDB("medicare_hospital_db");
db.doctors.createIndex({ specialization: 1, offersVideoConsultations: 1 });
db.patients.createIndex({ "appointments.appointmentStart": 1 });
db.pharmacies.createIndex({ location: "2dsphere" });
db.nurses.createIndex({ specialty: 1, isActive: 1 });
db.nurseCareRequests.createIndex({ patientId: 1, plannedStartDate: 1 });
db.nurseCareRequests.createIndex({ nurseId: 1, plannedStartDate: 1 });

