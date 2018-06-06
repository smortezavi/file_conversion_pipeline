import psycopg2

conn = psycopg2.connect("dbname=postgres user=postgres password=admin_post")
cur = conn.cursor()


cur.execute("""
	CREATE TABLE QIPM.Micro (
	Micro_EntryID integer,
	MRN text,
	Micro_ProcedureID integer,
	Micro_OrderDate date,
	Micro_CollectDateTime date,
	Micro_ResultDateTime date,
	Micro_Test text,
	Micro_Specimen text,
	Micro_ResultingLab text,
	Micro_OrderingProvider text,
	Micro_OrderingProviderSpecialty text,
	Micro_CultureComment text,
	Micro_OrderStatus text,
	Micro_Component text,
	Micro_Result text
	)
	""")
conn.commit()

cur.execute("""
	COPY QIPM.Micro
FROM
    '/tmp/Micro.csv' DELIMITER ',' CSV HEADER;
""")
conn.commit()

conn.close()


