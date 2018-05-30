import psycopg2

conn = psycopg2.connect("dbname=siavash_database")
cur = conn.cursor()


cur.execute("""
	CREATE TABLE new_schema.Medication (
	Medication_EntryID integer primary key,
	MRN integer,
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
	COPY new_schema.Medication
FROM
    '/Users/siavashmortezavi/Documents/UCSF/file_conversion_pipeline/csv/Medication.csv' DELIMITER ',' CSV HEADER;
""")
conn.commit()

conn.close()

