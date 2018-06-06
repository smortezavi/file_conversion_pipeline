import psycopg2

conn = psycopg2.connect("dbname=postgres user=postgres password=admin_post")
cur = conn.cursor()


cur.execute("""
	CREATE TABLE QIPM.Medication (
	Medication_EntryID integer,
	MRN text,
	Medication_OrderMedID integer,
	Medication_OrderInstitution date,
	Medication_Name text,
	Medication_StartDate date,
	Medication_EndDate date,
	Medication_AdminDate date,
	Medication_LastAdminDate date,
	Medication_Strength text,
	Medication_Form text,
	Medication_Route text,
	Medication_TheraClass text,
	Medication_Action text
	)
	""")
conn.commit()

cur.execute("""
	COPY QIPM.Medication
FROM
    '/tmp/Medication.csv' DELIMITER ',' CSV HEADER;
""")
conn.commit()

conn.close()

