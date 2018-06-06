import psycopg2

conn = psycopg2.connect("dbname=siavash_database")
cur = conn.cursor()


cur.execute("""
	CREATE TABLE new_schema.SurgicalHistory (
	SurgicalHistory_EntryID integer,
	MRN text,
	SurgicalHistory_ProcedureName text,
	SurgicalHistory_Laterality text,
	SurgicalHistory_SurgicalHxDate text,
	SurgicalHistory_Comments text
	)
	""")
conn.commit()

cur.execute("""
	COPY new_schema.SurgicalHistory
FROM
    '/Users/siavashmortezavi/Documents/UCSF/file_conversion_pipeline/csv/Surgical_History.csv' DELIMITER ',' CSV HEADER;
""")
conn.commit()

conn.close()



