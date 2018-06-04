import pandas as pd
import sys
import os


def xls_to_csv(path, destination, file):
	xls = pd.ExcelFile(path+file)
	#reads the entire xls as excelfile object

	sheets = xls.sheet_names
	#Puts all sheet names into a list

	print(f'converting excel file with name {file} and {len(sheets)} sheets into a csv file with 1 sheet')

	if len(sheets) == 1:
	    xls.parse(sheets[0]).to_csv(destination + file[:-4] + '.csv', encoding = 'utf-8')
	else:
	    final_df = xls.parse(sheets[0])
	    headers = final_df.columns
	    for i in range(1, len(sheets)):
	        temp_df = xls.parse(sheets[i], header=None, names=headers)
	        final_df = pd.concat([final_df, temp_df], ignore_index=True)
	    final_df.to_csv(destination + file[:-4] + '.csv', encoding = 'utf-8')
	print('done')

	
def dir_xls_to_csv(path, destination, xls_files):
	for file in xls_files:
		xls_to_csv(path, destination, file)

if __name__ == "__main__":
	PATH = sys.argv[1]
	DEST = sys.argv[2]
	xls_files = os.listdir(PATH)
	dir_xls_to_csv(PATH, DEST, xls_files)