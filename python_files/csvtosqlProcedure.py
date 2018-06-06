import psycopg2

conn = psycopg2.connect("dbname=postgres user=postgres password=admin_post")
cur = conn.cursor()


cur.execute("""
	CREATE TABLE new_schema.Procedure (
	Procedure_EntryID integer,
	MRN text,
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
	COPY QIPM.Procedures
FROM
    '/tmp/Procedures.csv' DELIMITER ',' CSV HEADER;
""")
conn.commit()

conn.close()



