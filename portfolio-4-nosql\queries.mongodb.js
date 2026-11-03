// Select medicare_hospital_db in Compass/mongosh before running these examples.
// Find active pharmacies within 10 km, nearest first.
// GeoJSON order is [longitude, latitude]. Sample origin only; do not store it.
db.pharmacies.find({
  isActive: true,
  location: {
    $near: {
      $geometry: { type: "Point", coordinates: [3.3792, 6.5244] },
      $maxDistance: 10000
    }
  }
});

// Patient's video consultation timeline, including the linked prescription.
db.patients.find(
  { _id: "DEMO-PAT-001" },
  { firstName: 1, lastName: 1, "appointments.consultationMode": 1,
    "appointments.appointmentStart": 1, "appointments.doctorId": 1,
    "appointments.prescriptions": 1 }
);

// Nurse's schedule plus the clinician-authored prescription it references.
db.nurseCareRequests.aggregate([
  { $match: {
      nurseId: "DEMO-NURSE-001",
      status: { $in: ["requested", "accepted", "active"] }
  }},
  { $lookup: { from: "patients", localField: "patientId", foreignField: "_id", as: "patient" } },
  { $unwind: "$patient" },
  { $unwind: "$patient.appointments" },
  { $unwind: "$patient.appointments.prescriptions" },
  { $match: { $expr: {
      $eq: ["$prescriptionId", "$patient.appointments.prescriptions.prescriptionId"]
  }}},
  { $project: {
      patientId: 1,
      nurseId: 1,
      plannedStartDate: 1,
      plannedEndDate: 1,
      visitFrequency: 1,
      careVisits: 1,
      clinicianPrescription: "$patient.appointments.prescriptions"
  }}
]);

// The nurse follows clinician-authored directions; the platform does not infer
// or alter a regimen from the diagnosis.

