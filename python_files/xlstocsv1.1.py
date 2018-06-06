import pandas as pd
import sys
import os
import psycopg2
import datetime

conn = psycopg2.connect("dbname=postgres user=olivier password=qipm123")
cur = conn.cursor()


def xls_to_csv(path, destination, file):
	xls = pd.ExcelFile(path+file)
	#reads the entire xls as excelfile object

	sheets = xls.sheet_names
	#Puts all sheet names into a list

	print(f'converting excel file with name {file} and {len(sheets)} sheets into a csv file with 1 sheet')

	if len(sheets) == 1:
		final_df = xls.parse(sheets[0])
		final_df['time_stamp'] = str(datetime.datetime.now())
		print(final_df.head(2))
		final_df.to_csv(destination + file.split()[2] + '.csv', encoding = 'utf-8')
	else:
	    final_df = xls.parse(sheets[0])
	    headers = final_df.columns
	    for i in range(1, len(sheets)):
	        temp_df = xls.parse(sheets[i], header=None, names=headers)
	        final_df = pd.concat([final_df, temp_df], ignore_index=True)
	    final_df['time_stamp'] = str(datetime.datetime.now())
	    print('i got here')
	    print(final_df.head(2))
	    final_df.to_csv(destination + file.split()[2] + '.csv', encoding = 'utf-8')
	print('done with csv conversion')
	print('begin loading into data base')
	file_path = "'" + destination + file.split()[2] + '.csv' + "'"
	
	
	table_to_sql_dict = {'Allergy':f"COPY qipm.Allergy FROM {file_path} DELIMITER ',' CSV HEADER;",
 'Encounters':f"COPY qipm.Encounters FROM {file_path} DELIMITER ',' CSV HEADER;",
 'Family':f"COPY qipm.FamilyHistory FROM {file_path} DELIMITER ',' CSV HEADER;",
 'Imaging':f"COPY qipm.Imaging FROM {file_path} DELIMITER ',' CSV HEADER;",
 'Labs':f"COPY qipm.Labs FROM {file_path} DELIMITER ',' CSV HEADER;",
 'Medical':f"COPY qipm.MedicalHistory FROM {file_path} DELIMITER ',' CSV HEADER;",
 'Medication':f"COPY qipm.Medication FROM {file_path} DELIMITER ',' CSV HEADER;",
 'Micro':f"COPY qipm.Micro FROM {file_path} DELIMITER ',' CSV HEADER;",
 'Notes':f"COPY qipm.Notes FROM {file_path} DELIMITER ',' CSV HEADER;",
 'Pathology':f"COPY qipm.Pathology FROM {file_path} DELIMITER ',' CSV HEADER;",
 'Patient':f"COPY qipm.Demographic FROM {file_path} DELIMITER ',' CSV HEADER;",
 'Problem':f"COPY qipm.ProblemList FROM {file_path} DELIMITER ',' CSV HEADER;",
 'Procedures':f"COPY qipm.Procedure FROM {file_path} DELIMITER ',' CSV HEADER;",
 'Social':f"COPY qipm.SocialHistory FROM {file_path} DELIMITER ',' CSV HEADER;",
 'Surgical':f"COPY qipm.SurgicalHistory FROM {file_path} DELIMITER ',' CSV HEADER;"}

 	
 	#Loading table
 	
	print('')
	print(f"""{table_to_sql_dict[file.split()[2]]}""")
	print('')
	cur.execute(f"""{table_to_sql_dict[file.split()[2]]}""")
	conn.commit()


	
def dir_xls_to_csv(path, destination, xls_files):
	for file in xls_files:
		xls_to_csv(path, destination, file)

if __name__ == "__main__":
	PATH = sys.argv[1]
	DEST = sys.argv[2]
	xls_files = os.listdir(PATH)
	dir_xls_to_csv(PATH, DEST, xls_files)
	conn.close()