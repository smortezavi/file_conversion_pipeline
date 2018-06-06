import psycopg2

conn = psycopg2.connect("dbname=siavash_database")
cur = conn.cursor()

cur.execute("""
	CREATE TABLE new_schema.Allergy (
    Encounter_UniqueID integer,
    MRN text,
    Allergy_Allergen text,
	Allergy_DateNoted date,
	Allergy_Reaction text,
	Allergy_Severity text)
	""")
conn.commit()

cur.execute("""
	COPY new_schema.Allergy
FROM
    '//Users/siavashmortezavi/Documents/UCSF/file_conversion_pipeline/csv/Allergy.csv' DELIMITER ',' CSV HEADER;
""")
conn.commit()

conn.close()


