-- Run while connected to medicare_hospital_db.
-- 1) Representative patient-history query; capture its output.
SELECT p.patient_id, p.first_name, p.last_name,
       a.appointment_start, a.status, d.specialization,
       mr.diagnosis
FROM patients AS p
JOIN appointments AS a ON a.patient_id = p.patient_id
JOIN doctors AS d ON d.doctor_id = a.doctor_id
LEFT JOIN medical_records AS mr ON mr.appointment_id = a.appointment_id
WHERE p.email = 'ada.nwosu@example.test'
ORDER BY a.appointment_start DESC;

-- 2) Baseline plan. EXPLAIN ANALYZE executes the read-only SELECT and reports
-- actual runtime/rows as well as the planner's estimated cost.
EXPLAIN (ANALYZE, BUFFERS, VERBOSE)
SELECT appointment_id, appointment_start, status
FROM appointments
WHERE patient_id = (SELECT patient_id FROM patients WHERE email = 'ada.nwosu@example.test')
ORDER BY appointment_start DESC;

-- 3) A covering lookup index for this patient-history access pattern.
-- IF NOT EXISTS makes repeated runs safe. Compare plans before/after; on the
-- tiny demo PostgreSQL may correctly prefer a sequential scan.
CREATE INDEX IF NOT EXISTS idx_appointments_patient_start
    ON appointments (patient_id, appointment_start DESC)
    INCLUDE (status);

ANALYZE appointments;

EXPLAIN (ANALYZE, BUFFERS, VERBOSE)
SELECT appointment_id, appointment_start, status
FROM appointments
WHERE patient_id = (SELECT patient_id FROM patients WHERE email = 'ada.nwosu@example.test')
ORDER BY appointment_start DESC;

-- 4) A partial index covers completed-payment lookups only.
CREATE INDEX IF NOT EXISTS idx_payments_completed_billing
    ON payments (billing_id) INCLUDE (amount)
    WHERE status = 'completed';

EXPLAIN (ANALYZE, BUFFERS, VERBOSE)
SELECT billing_id, SUM(amount) AS paid_amount
FROM payments
WHERE status = 'completed'
GROUP BY billing_id;

-- Capture the actual plans and timings from this machine in evidence/.

