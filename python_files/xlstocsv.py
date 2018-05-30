import xlrd
import csv



def csv_from_excel():
	
	wb = xlrd.open_workbook('HISTORICAL RadOnc Patient Demo Extract REP0065032.xls')
	print(wb)
	sh = wb.sheet_by_name('Sheet1')
	your_csv_file = open('/tmp/test.csv', 'w')
	wr = csv.writer(your_csv_file, quoting =csv.QUOTE_ALL)
	
	for rownum in range(sh.nrows):
		wr.writerow(sh.row_values(rownum))
	
	your_csv_file.close()
	
	
if __name__ == "__main__":
	csv_from_excel()