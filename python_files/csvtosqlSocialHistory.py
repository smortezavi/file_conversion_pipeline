import psycopg2

conn = psycopg2.connect("dbname=siavash_database")
cur = conn.cursor()


cur.execute("""
	CREATE TABLE new_schema.SocialHistory (
	SocialHistory_EntryID integer,
	MRN text,
	SocialHistory_SmokingStatus text,
	SocialHistory_CigarettesYN text,
	SocialHistory_CigarsYN text,
	SocialHistory_PipesYN text,
	SocialHistory_TobaccoPackPerDay numeric,
	SocialHistory_TobaccoUsedYears numeric,
	SocialHistory_TobaccoComment text,
	SocialHistory_AlcoholUse text,
	SocialHistory_AlcoholOzPerWeek text,
	SocialHistory_AlcoholComment text,
	SocialHistory_YearsEducation numeric,
	SocialHistory_IllicitDrugUserYN text,
	SocialHistory_IllicitDrugFreq text,
	SocialHistory_IllicitDrugComment text,
	SocialHistory_SexuallyActiveYN text,
	SocialHistory_PatEncCsnID integer,
	SocialHistory_ContactDate date
	)
	""")
conn.commit()

cur.execute("""
	COPY new_schema.SocialHistory
FROM
    '/Users/siavashmortezavi/Documents/UCSF/file_conversion_pipeline/csv/Social_History.csv' DELIMITER ',' CSV HEADER;
""")
conn.commit()

conn.close()



