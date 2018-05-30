import psycopg2

conn = psycopg2.connect("dbname=siavash_database")
cur = conn.cursor()


cur.execute("""
	CREATE TABLE new_schema.Procedure (
	Procedure_EntryID integer primary key,
	MRN integer,
	Procedure_OrderDate date,
	Procedure_Description text,
	Procedure_Specialty text,
	Procedure_Status text,
	Procedure_OrderingProvider text,
	Procedure_ResultDateTime date,
	Procedure_ProcedureNote text,
	Procedure_OrderQuestions text,
	Procedure_OrderProcedureID integer
	)
	""")
conn.commit()

cur.execute("""
	COPY new_schema.Procedure
FROM
    '/Users/siavashmortezavi/Documents/UCSF/file_conversion_pipeline/csv/Procedure.csv' DELIMITER ',' CSV HEADER;
""")
conn.commit()

conn.close()



