import psycopg2

conn = psycopg2.connect("dbname=postgres user=postgres password=admin_post")
cur = conn.cursor()


cur.execute("""
	CREATE TABLE QIPM.Demographic (
	Deomgraphic_EntryID integer,
	MRN text primary key,
	Demographic_FirstName text,
	Demographic_LastName text,
	Demographic_DOB date,
	Demographic_Sex text,
	Demographic_Race text,
	Demographic_StreetAddress text,
	Demographic_City text,
	Demographic_State text,
	Demographic_Zip text,
	Demographic_HomePhone text,
	Demographic_CellPhone text,
	Demographic_WorkPhone text,
	Demographic_EmergencyContactName text,
	Demographic_EmergencyContactRelation text,
	Demographic_EmergencyContactHomePhone text, 
	Demographic_EmergencyContactCellPhone text,
	Demographic_EmergencyContactWorkPhone text,
	Demographic_Email text,
	Demographic_Occupation text,
	Demographic_Employer text,
	Demographic_MaritalStatus text,
	Demographic_PreferredLanguage text,
	Demographic_InterpreterNeeded text,
	Demographic_Status text,
	Demographic_DateOfDeath text,
	Demographic_InsuranceName text
	)
	""")
conn.commit()

cur.execute("""
	COPY  QIPM.Demographic
FROM
    '/tmp/Demographic.csv' DELIMITER ',' CSV HEADER;
""")
conn.commit()

conn.close()



