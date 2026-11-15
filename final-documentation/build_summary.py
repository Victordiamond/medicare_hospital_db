from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from pathlib import Path


OUT = Path(__file__).resolve().with_name("MIT-8103-MediCare-Portfolio-Summary-DRAFT.docx")
doc = Document()
sec = doc.sections[0]
sec.top_margin = Inches(0.62)
sec.bottom_margin = Inches(0.62)
sec.left_margin = Inches(0.72)
sec.right_margin = Inches(0.72)

normal = doc.styles["Normal"]
normal.font.name = "Arial"
normal.font.size = Pt(9.5)
normal.font.color.rgb = RGBColor(35, 43, 52)
normal.paragraph_format.space_after = Pt(4)
normal.paragraph_format.line_spacing = 1.05
for style_name, size in [("Heading 1", 13), ("Heading 2", 10.5)]:
    s = doc.styles[style_name]
    s.font.name = "Arial"
    s.font.size = Pt(size)
    s.font.bold = True
    s.font.color.rgb = RGBColor(22, 67, 99)
    s.paragraph_format.space_before = Pt(7)
    s.paragraph_format.space_after = Pt(3)
title = doc.styles["Title"]
title.font.name = "Arial"
title.font.size = Pt(20)
title.font.bold = True
title.font.color.rgb = RGBColor(22, 67, 99)
title.paragraph_format.space_after = Pt(3)

p = doc.add_paragraph(style="Title")
p.add_run("MIT 8103 Advanced Database Portfolio")
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.LEFT
r = p.add_run("MediCare Hospital Management System | Telemedicine Case Study")
r.bold = True
r.font.color.rgb = RGBColor(82, 100, 114)

p = doc.add_paragraph()
p.add_run("Student: ").bold = True
p.add_run("[Your name and student ID]     ")
p.add_run("Session: ").bold = True
p.add_run("2026/2027 First Semester")
p = doc.add_paragraph()
p.add_run("GitHub: ").bold = True
p.add_run("https://github.com/Victordiamond/medicare_hospital_301911811")

doc.add_paragraph("This portfolio models MediCare as a simulated telemedicine service. Patients find doctors, book video consultations, share symptoms, and receive prescriptions. They can search nearby pharmacies or select a nurse for prescription-linked visits over a planned care period. The relational and document databases use fictional coursework data only.")

doc.add_heading("Portfolio 1  Database design and modelling", level=1)
doc.add_paragraph("The PostgreSQL schema separates patients, doctors, consultations, medical records, prescriptions, pharmacy fulfillment, nurses, care requests, nurse visits, billing, and payments. Foreign keys keep links valid; unique constraints prevent duplicate identities, payment references, and exact appointment slots; check constraints limit workflow states and invalid values. Nurse care requests are separate from individual visits so one plan can contain multiple bookings. Bills and payment events are separate so one consultation charge can be settled in installments. Pharmacy latitude and longitude support proximity search; the patient's live map position is supplied for a search instead of stored in the database.")
doc.add_paragraph("The schema ran in pgAdmin and the consultation report returned two fictional rows. Both appointment symptom summaries are blank in the saved sample, so the output does not yet demonstrate symptom capture. Pharmacy-distance and nurse-schedule query outputs and screenshots still need saving. ER diagram and schema: portfolio-1-database-design/. Explain in your own words: [why the consultation and care-request relationships suit the platform, and one 3NF decision].")

doc.add_heading("Portfolio 2  Query processing and optimisation", level=1)
doc.add_paragraph("The SQL file contains a patient-history report and a separate measured appointment lookup filtered by patient and sorted by time. A composite patient/time index targets that lookup; a partial covering index was tested for completed-payment totals. On the two-appointment sample, the baseline used Seq Scan plus Sort (1 estimated and actual row, 3 shared-buffer hits, 0.068 ms). After index creation, PostgreSQL still used Seq Scan plus Sort (3 shared-buffer hits, 0.087 ms). It also used a sequential scan and hash aggregate for the one-payment total (0.091 ms). The appointment and payment indexes were not selected. These tiny timings do not show a speedup. Raw plans: evidence/portfolio-2/.")

doc.add_heading("Portfolio 3  Transactions and concurrency", level=1)
doc.add_paragraph("A temporary table demonstrated COMMIT, savepoint rollback, and full rollback without changing hospital records; the final result contained only event 1, 'committed example'. In the two-session READ COMMITTED row-lock exercise, Session B waited about 26 seconds while Session A held nurse visit 1 with SELECT FOR UPDATE. After A committed, B's update completed and was rolled back. An accidentally queued duplicate update was also rolled back; the final fresh query returned nurse visit 1 as booked. CSVs, the observed sequence, and the final-query screenshot are in evidence/portfolio-3/; the screenshot is uploaded to GitHub.")

doc.add_heading("Portfolio 4  NoSQL and advanced data models", level=1)
doc.add_paragraph("MongoDB embeds consultation history and prescription details in a patient document for patient-centered reads. Doctors, nurses, and pharmacies remain separate collections. Pharmacy GeoJSON points use a 2dsphere index for nearest-location search; nurse care requests reference the patient and prescription and embed a bounded list of visit slots. This reduces lookups for these reads but means the application must keep cross-document references consistent. The map query finds nearby points; actual road directions belong to a mapping service.")
doc.add_paragraph("The Compass evidence records 2 patients, 2 doctors, 2 pharmacies, 2 nurses, and 1 nurse-care request with two visits. Six secondary indexes were confirmed; nearest-pharmacy search returned Yaba then Ikeja; the nurse aggregation returned two booked visits and prescription DEMO-RX-001. The geospatial plan selected location_2dsphere and returned two pharmacies after examining four keys and four documents in 9 ms. This is a two-pharmacy demo, not a production benchmark. One stale fictional patient document lacked prescriptionId; one updateOne corrected it and the rerun succeeded. A Compass connection/explain screenshot is uploaded to evidence/portfolio-4/; focused document and nurse-result screenshots remain pending.")

doc.add_heading("Portfolio 5  Distributed and cloud database exercise", level=1)
doc.add_paragraph("The design proposes a PostgreSQL primary for correctness-sensitive writes, a standby, a read-only replica for stale-tolerant search/reporting, and a MongoDB replica set for patient-history documents. It discusses synchronous/asynchronous trade-offs, replica lag, fencing, backups, and scale-out choices. This is design evidence only: no cloud service, replica lag, failover, or restore drill was deployed or tested.")

doc.add_heading("Individual technical reflection", level=1)
doc.add_paragraph("[Write this yourself from your work: one problem you actually encountered, how you diagnosed it, which evidence demonstrates the result, a design choice you would revisit, and what you learned. Do not invent experience.]")

doc.add_heading("AI use and references", level=1)
doc.add_paragraph("AI-use declaration: I used ChatGPT to organise the CA requirements, explain database design options, and prepare example SQL and documentation. I personally [state which files you ran and reviewed, corrections you made, and analysis/reflection you wrote]. I verified my submitted results using [identify actual screenshots, query outputs, or plans]. Add every course source, technical reference, dataset, and other tool actually used. Amend this statement so it accurately describes your contribution.")
doc.add_paragraph("References: [list course materials, PostgreSQL and MongoDB documentation, and other sources you actually consulted, in the required citation style].")

footer = sec.footer.paragraphs[0]
footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = footer.add_run("MediCare telemedicine database portfolio  |  Working draft")
run.font.name = "Arial"
run.font.size = Pt(8)
run.font.color.rgb = RGBColor(100, 110, 120)

doc.core_properties.title = "MIT 8103 MediCare Telemedicine Portfolio Summary Draft"
doc.core_properties.subject = "Continuous assessment portfolio summary"
doc.core_properties.author = ""
doc.save(OUT)
print(OUT)

