import pandas as pd
file = 'crawling/restaurant list.xlsx'
xlsx = pd.read_excel(file,sheet_name = 0, header = 0)
print(xlsx)