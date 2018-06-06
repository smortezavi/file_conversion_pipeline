import psycopg2

conn = psycopg2.connect("dbname=postgres user=olivier password=qipm123")
cur = conn.cursor()




cur.execute("""
DROP TABLE qipm.ProblemList
""")

conn.commit()

cur.execute("""
	CREATE TABLE qipm.ProblemList (
	ProblemList_EntryID integer,
	MRN text,
	ProblemList_Condition  text,
	ProblemList_DateNoted date,
	ProblemList_DateResolved date,
	ProblemList_ICD9CM text,
	Date_created date
	)
	""")
conn.commit()

cur.execute("""
	COPY qipm.ProblemList
FROM
    '/Users/olivier/Documents/Vash_Code/test/csv/Problem.csv' DELIMITER ',' CSV HEADER;
""")
conn.commit()

conn.close()

