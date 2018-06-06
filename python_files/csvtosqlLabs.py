import psycopg2

conn = psycopg2.connect("dbname=siavash_database")
cur = conn.cursor()


cur.execute("""
	CREATE TABLE new_schema.Labs (
	Labs_EntryID integer,
	MRN text,
	Labs_ProcedureOrderID integer,
	Labs_ProcedureDate date,
	Labs_ResultDate date,
	Labs_TestName text,
	Labs_LineNumberDetails integer,
	Labs_LabResultName text,
	Labs_LabResultValue numeric,
	Labs_ReferenceLow numeric,
	Labs_ReferenceHigh numeric,
	Labs_ResultInRange text,
	Labs_CollectDate date, 
	Labs_CollectTime date,
	Labs_Specimen text,
	Labs_ResultingLab text,
	Labs_OrderingProvider text,
	Labs_OrderingProviderSpecialty text,
	Labs_OrderStatus text
	)
	""")
conn.commit()

cur.execute("""
	COPY new_schema.Labs
FROM
    '/Users/siavashmortezavi/Documents/UCSF/file_conversion_pipeline/csv/Labs.csv' DELIMITER ',' CSV HEADER;
""")
conn.commit()

conn.close()


