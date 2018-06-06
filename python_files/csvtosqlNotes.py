import psycopg2

conn = psycopg2.connect("dbname=siavash_database")
cur = conn.cursor()


cur.execute("""
	CREATE TABLE new_schema.Notes (
	Notes_EntryID integer,
	MRN text,
	Notes_NoteID integer,
	Notes_FilingDate date,
	Notes_ServiceDate date,
	Notes_NoteType text,
	Notes_Department text,
	Notes_Service text,
	Notes_Author text,
	Notes_AuthorType text,
	Notes_Status text,
	Notes_NoteContent text
	)
	""")
conn.commit()

cur.execute("""
	COPY new_schema.Notes
FROM
    '/Users/siavashmortezavi/Documents/UCSF/file_conversion_pipeline/csv/Notes.csv' DELIMITER ',' CSV HEADER;
""")
conn.commit()

conn.close()


