import psycopg2

conn = psycopg2.connect("dbname=postgres user=postgres password=admin_post")
cur = conn.cursor()


cur.execute("""
	CREATE TABLE QIPM.Pathology (
	Pathology_EntryID integer,
	MRN text,
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
	COPY QIPM.Pathology
FROM
    '/tmp/Pathology.csv' DELIMITER ',' CSV HEADER;
""")
conn.commit()

conn.close()


