import psycopg2

conn = psycopg2.connect("dbname=siavash_database")
cur = conn.cursor()


cur.execute("""
	CREATE TABLE new_schema.Encounters (
    Encounter_EntryID integer,
    MRN text,
    Encounter_UniqueID integer,
    Encounter_Date date,
	Encounter_Status text,
	Encounter_Type text,
	Encounter_Department text,
	Encounter_Specialty text,
	Encounter_Provider text,
	Encounter_HeightLength text,
	Encounter_SystolicBloodPressure numeric,
	Encounter_DiastolicBloodPressure numeric,
	Encounter_Pulse numeric,
	Encounter_Respirations numeric,
	Encounter_Weight numeric)
	""")
conn.commit()

cur.execute("""
	COPY new_schema.Encounters
FROM
    '/Users/siavashmortezavi/Documents/UCSF/file_conversion_pipeline/csv/Encounters.csv' DELIMITER ',' CSV HEADER;
""")
conn.commit()

conn.close()