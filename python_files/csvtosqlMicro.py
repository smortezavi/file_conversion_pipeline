import psycopg2

conn = psycopg2.connect("dbname=siavash_database")
cur = conn.cursor()


cur.execute("""
	CREATE TABLE new_schema.Micro (
	Micro_EntryID integer primary key,
	MRN integer,
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
	COPY new_schema.Micro
FROM
    '/Users/siavashmortezavi/Documents/UCSF/file_conversion_pipeline/csv/Micro.csv' DELIMITER ',' CSV HEADER;
""")
conn.commit()

conn.close()

