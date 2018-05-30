import psycopg2

conn = psycopg2.connect("dbname=siavash_database")
cur = conn.cursor()


cur.execute("""
	CREATE TABLE new_schema.Family_History (
	FamilyHistory_EntryID integer primary key,
	MRN integer,
    FamilyHistory_Problem text,
    FamilyHistory_Relation text,
	FamilyHistory_FamilyName text,
	FamilyHistory_AgeOfOnset numeric,
	FamilyHistory_Comments text)
	""")
conn.commit()

cur.execute("""
	COPY new_schema.Family_History
FROM
    '/Users/siavashmortezavi/Documents/UCSF/file_conversion_pipeline/csv/Family_History.csv' DELIMITER ',' CSV HEADER;
""")
conn.commit()

conn.close()