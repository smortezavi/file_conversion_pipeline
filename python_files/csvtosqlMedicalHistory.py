import psycopg2

conn = psycopg2.connect("dbname=siavash_database")
cur = conn.cursor()


cur.execute("""
	CREATE TABLE new_schema.MedicalHistory (
	MedicalHistory_EntryID integer primary key,
	MRN integer,
	MedicalHistory_DxID integer,
	MedicalHistory_ICD9Code integer,
	MedicalHistory_DxName text,
	MedicalHistory_MedHistDate text,
	MedicalHistory_Comments text,
	MedicalHistory_ConctactDate date,
	MedicalHistory_Line integer
	)
	""")
conn.commit()

cur.execute("""
	COPY new_schema.MedicalHistory
FROM
    '/Users/siavashmortezavi/Documents/UCSF/file_conversion_pipeline/csv/Medical_History.csv' DELIMITER ',' CSV HEADER;
""")
conn.commit()

conn.close()
