import psycopg2

conn = psycopg2.connect("dbname=siavash_database")
cur = conn.cursor()

cur.execute("""
	CREATE TABLE new_schema.Allergy (ID integer,
    Allergy_EntryID integer PRIMARY KEY,
    Allergy_Allergen text,
	Allergy_DateNoted date,
	Allergy_Reaction text,
	Allergy_Severity text)
	""")
conn.commit()

cur.execute("""
	COPY new_schema.Allergy
FROM
    '/Users/siavashmortezavi/Desktop/Allergy.csv' DELIMITER ',' CSV HEADER;
""")
conn.commit()

conn.close()