import pandas as pd
import sys

data_xls = pd.read_excel(sys.argv[1], 'Sheet1', index_col=None)
data_xls.to_csv('your_csv.csv', encoding = 'utf-8')

