import psycopg2

conn = psycopg2.connect("dbname=postgres user=postgres password=admin_post")
cur = conn.cursor()


cur.execute("""
	CREATE TABLE QIPM.Imaging (
	Imaging_EntryID integer primary key,
	MRN integer,
	Imaging_OrderProcID text,
    Imaging_OrderedDate date,
    Imaging_ExamDate date,
	Imaging_Exam text,
	Imaging_AccessionNumber text,
	Imaging_OrderClass text,
	Imaging_Medication text,
	Imaging_Route text,
	Imaging_AdminDose text,
	Imaging_Volume text,
	Imaging_LastAdminTime text,
	Imaging_NumberOfDoses text,
	Imaging_StudyResult	text,
	Imaging_EntryDateAndTime date,
	Imaging_Status text,
	Imaging_ResultNarrative text,
	Imaging_ResultImpression text
	)
	""")
conn.commit()

cur.execute("""
	COPY QIPM.Imaging
FROM
    '/tmp/Imaging.csv' DELIMITER ',' CSV HEADER;
""")
conn.commit()

conn.close()


