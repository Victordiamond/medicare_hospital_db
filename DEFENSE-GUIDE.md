# MediCare portfolio — defense guide

Use the evidence from your own runs. These prompts help you explain the work; they are not substitute answers for results you have not observed.

## Portfolio 1: design

- **Why is this MediCare telemedicine?** Patients book online video consultations, doctors record visits and prescribe, pharmacy orders link to prescriptions, and nurse visits follow prescription-linked care requests.
- **Why separate `nurse_care_requests` and `nurse_visits`?** One request can schedule many visits; storing the repeated sessions separately in SQL avoids repeating request details and allows each slot to have its own status.
- **Why keep `billing` and `payments` separate?** One bill can be paid in multiple payments, and payment events need their own references, methods, timestamps, and statuses.
- **What enforces correctness?** Describe one foreign key (keeps a reference valid), one unique constraint (prevents duplicates), and one check constraint (restricts values).
- **What is not implemented?** A real video-call service and turn-by-turn map routing are external app integrations. SQL stores the meeting reference and pharmacy coordinates.

## Portfolio 2: query optimization

- Read the actual `EXPLAIN ANALYZE` plan: name the scan/join nodes, compare estimated and actual rows, buffers, and time.
- Explain why `(patient_id, appointment_start DESC)` matches a patient's recent-consultation lookup.
- If PostgreSQL still chooses a sequential scan, explain that the demo is tiny and sequential access can cost less than traversing an index.
- Explain that indexes use storage and add write work; recommend based on measured access patterns, not on index presence alone.

## Portfolio 3: transactions and concurrency

- Explain which temporary row survives the savepoint rollback and commit, and which row disappears after full rollback.
- Describe the two-session `FOR UPDATE` observation: a conflicting update waits until the lock holder commits; then the second transaction continues.
- State the isolation level you actually used and whether the booking update was rolled back.

## Portfolio 4: NoSQL

- Explain why consultation history and a bounded nurse visit schedule are embedded for parent-centered reads.
- Explain why doctors, nurses, and pharmacies are separate documents and how the application maintains references between collections.
- GeoJSON coordinates are stored longitude first, latitude second. A `2dsphere` index enables nearest-pharmacy search; it does not calculate road routes.
- Name one advantage and one limitation versus the relational schema.

## Portfolio 5: distributed/cloud

- Explain why the PostgreSQL primary is authoritative for appointments, prescriptions, nurse bookings, billing, and payments; the patient history in MongoDB is a projection and needs an idempotent outbox consumer.
- Distinguish stale-tolerant browsing/reporting from availability checks and read-after-write confirmation, which should use the authoritative store.
- Explain that synchronous replication can reduce acknowledged data loss at a latency/availability cost, while asynchronous replication can lag and lose recent changes if promoted.
- Describe fencing before standby promotion, backup/PITR for operator error, and why replica copies are not backups.
- Explain why this tiny demo does not justify sharding yet, and name one likely partition key plus its cross-shard cost if the service grows.
- State clearly that the portfolio presents a design. No cloud deployment, replica lag measurement, failover exercise, or restore drill has been performed.

## Student reflection

Be ready to describe a problem you actually encountered, how you found its cause, what evidence proves the fix, and what you would change next. Use your own work log; do not invent a debugging story.

