import psycopg2

conn = psycopg2.connect("dbname=siavash_database")
cur = conn.cursor()


cur.execute("""
	CREATE TABLE new_schema.ProblemList (
	ProblemList_EntryID integer primary key,
	MRN integer,
	ProblemList_Condition  text,
	ProblemList_DateNoted date,
	ProblemList_DateResolved date,
	ProblemList_ICD9CM text
	)
	""")
conn.commit()

cur.execute("""
	COPY new_schema.ProblemList
FROM
    '/Users/siavashmortezavi/Documents/UCSF/file_conversion_pipeline/csv/Problem_List.csv' DELIMITER ',' CSV HEADER;
""")
conn.commit()

conn.close()



