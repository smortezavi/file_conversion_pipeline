import psycopg2

conn = psycopg2.connect("dbname=postgres user=olivier password=qipm123")
cur = conn.cursor()


cur.execute("""
DROP TABLE qipm.Allergy
""")

conn.commit()

cur.execute("""
	CREATE TABLE qipm.Allergy (
    Encounter_UniqueID integer,
    MRN text,
    Allergy_Allergen text,
	Allergy_DateNoted date,
	Allergy_Reaction text,
	Allergy_Severity text,
	Allergy_DateEntryLoaded date
	)
	""")
conn.commit()

cur.execute("""
DROP TABLE qipm.Demographic
""")

conn.commit()

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
	Demographic_InsuranceName text,
	Demographic_DateEntryLoaded date
	)
	""")
conn.commit()

cur.execute("""
DROP TABLE qipm.Encounters
""")

conn.commit()

cur.execute("""
	CREATE TABLE qipm.Encounters (
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
	Encounter_Weight numeric,
	Encounter_DateEntryLoaded date
	)
	""")
conn.commit()

cur.execute("""
DROP TABLE qipm.FamilyHistory
""")

conn.commit()

cur.execute("""
	CREATE TABLE qipm.FamilyHistory (
	FamilyHistory_EntryID integer,
	MRN text,
    FamilyHistory_Problem text,
    FamilyHistory_Relation text,
	FamilyHistory_FamilyName text,
	FamilyHistory_AgeOfOnset numeric,
	FamilyHistory_Comments text,
	FamilyHistory_DateEntryLoaded date
	)
	""")
conn.commit()

cur.execute("""
DROP TABLE qipm.Imaging
""")

conn.commit()

cur.execute("""
	CREATE TABLE QIPM.Imaging (
	Imaging_EntryID integer,
	MRN text,
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
	Imaging_ResultImpression text,
	Imaging_DateEntryLoaded date
	)
	""")
conn.commit()

cur.execute("""
DROP TABLE qipm.Labs
""")

conn.commit()

cur.execute("""
	CREATE TABLE qipm.Labs (
	Labs_EntryID integer,
	MRN text,
	Labs_ProcedureOrderID integer,
	Labs_ProcedureDate date,
	Labs_ResultDate date,
	Labs_TestName text,
	Labs_LineNumberDetails integer,
	Labs_LabResultName text,
	Labs_LabResultValue text,
	Labs_ReferenceLow numeric,
	Labs_ReferenceHigh numeric,
	Labs_ResultInRange text,
	Labs_CollectDate date, 
	Labs_CollectTime date,
	Labs_Specimen text,
	Labs_ResultingLab text,
	Labs_OrderingProvider text,
	Labs_OrderingProviderSpecialty text,
	Labs_OrderStatus text,
	Labs_DateEntryLoaded date
	)
	""")
conn.commit()

cur.execute("""
DROP TABLE qipm.MedicalHistory
""")

conn.commit()

cur.execute("""
	CREATE TABLE qipm.MedicalHistory (
	MedicalHistory_EntryID integer,
	MRN text,
	MedicalHistory_DxID integer,
	MedicalHistory_ICD9Code integer,
	MedicalHistory_DxName text,
	MedicalHistory_MedHistDate text,
	MedicalHistory_Comments text,
	MedicalHistory_ConctactDate date,
	MedicalHistory_Line integer,
	MedicalHistory_DateEntryLoaded date
	)
	""")
conn.commit()

cur.execute("""
DROP TABLE qipm.Medication
""")

conn.commit()

cur.execute("""
	CREATE TABLE QIPM.Medication (
	Medication_EntryID integer,
	MRN text,
	Medication_OrderMedID integer,
	Medication_OrderInstitution date,
	Medication_Name text,
	Medication_StartDate date,
	Medication_EndDate date,
	Medication_AdminDate date,
	Medication_LastAdminDate date,
	Medication_Strength text,
	Medication_Form text,
	Medication_Route text,
	Medication_TheraClass text,
	Medication_Action text,
	Medication_DateEntryLoaded date
	)
	""")
conn.commit()

cur.execute("""
DROP TABLE qipm.Micro
""")

conn.commit()

cur.execute("""
	CREATE TABLE QIPM.Micro (
	Micro_EntryID integer,
	MRN text,
	Micro_ProcedureID integer,
	Micro_OrderDate date,
	Micro_CollectDateTime date,
	Micro_ResultDateTime date,
	Micro_Test text,
	Micro_Specimen text,
	Micro_ResultingLab text,
	Micro_OrderingProvider text,
	Micro_OrderingProviderSpecialty text,
	Micro_CultureComment text,
	Micro_OrderStatus text,
	Micro_Component text,
	Micro_Result text,
	Micro_DateEntryLoaded date
	)
	""")
conn.commit()

cur.execute("""
DROP TABLE qipm.Notes
""")

conn.commit()

cur.execute("""
	CREATE TABLE qipm.Notes (
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
	Notes_NoteContent text,
	Notes_DateEntryLoaded date
	)
	""")
conn.commit()

cur.execute("""
DROP TABLE qipm.Pathology
""")

conn.commit()

cur.execute("""
	CREATE TABLE QIPM.Pathology (
	Pathology_EntryID integer,
	MRN text,
	Pathology_OrderID integer,
	Pathology_CollectDateTime date,
	Pathology_ResultingAgency text,
	Pathology_Comments text,
	Pathology_ResultTime date,
	Pathology_Test text,
	Pathology_OrderQuestions text,
	Pathology_OrderQuestionResponse text,
	Pathology_OrderingProvider text,
	Pathology_OrderingProviderSpecialty text,
	Pathology_Impression text,
	Pathology_Comment text,
	Pathology_DateEntryLoaded date
	)
	""")
conn.commit()

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
	ProblemList_DateEntryLoaded date
	)
	""")
conn.commit()

cur.execute("""
DROP TABLE qipm.Procedure
""")

conn.commit()

cur.execute("""
	CREATE TABLE qipm.Procedure (
	Procedure_EntryID integer,
	MRN text,
	Procedure_OrderDate date,
	Procedure_Description text,
	Procedure_Specialty text,
	Procedure_Status text,
	Procedure_OrderingProvider text,
	Procedure_ResultDateTime date,
	Procedure_ProcedureNote text,
	Procedure_OrderQuestions text,
	Procedure_OrderProcedureID integer,
	Procedure_DateEntryLoaded date
	)
	""")
conn.commit()

cur.execute("""
DROP TABLE qipm.SocialHistory
""")

conn.commit()

cur.execute("""
	CREATE TABLE qipm.SocialHistory (
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
	SocialHistory_ContactDate date,
	SocialHistory_DateEntryLoaded date
	)
	""")
conn.commit()

cur.execute("""
DROP TABLE qipm.SurgicalHistory
""")

conn.commit()

cur.execute("""
	CREATE TABLE qipm.SurgicalHistory (
	SurgicalHistory_EntryID integer,
	MRN text,
	SurgicalHistory_ProcedureName text,
	SurgicalHistory_Laterality text,
	SurgicalHistory_SurgicalHxDate text,
	SurgicalHistory_Comments text,
	SurgicalHistory_DateEntryLoaded date
	)
	""")
conn.commit()

conn.close()