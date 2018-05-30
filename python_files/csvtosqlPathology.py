import psycopg2

conn = psycopg2.connect("dbname=siavash_database")
cur = conn.cursor()


cur.execute("""
	CREATE TABLE new_schema.Pathology (
	Pathology_EntryID integer primary key,
	MRN integer,
	Pathology_OrderID integer,
	Pathology_CollectDateTime date,
	Pathology_ResultingAgency text,
	Pathology_Comments text,
	Pathology_ResultTime date,
	Pathology_Test text,
	Pathology_OrderQuestions text,
	Pathology_OrderQuestionResponse text,
	Pathology_OrderingProvider text,
	Pathology_OrderingProviderSpecialty text,
	Pathology_Impression text,
	Pathology_Comment text
	)
	""")
conn.commit()

cur.execute("""
	COPY new_schema.Pathology
FROM
    '/Users/siavashmortezavi/Documents/UCSF/file_conversion_pipeline/csv/Pathology.csv' DELIMITER ',' CSV HEADER;
""")
conn.commit()

conn.close()


