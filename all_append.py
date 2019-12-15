###########################Devanshi####################
import glob
import pandas as pd
path = "C:/Users"
file_identifier = "*.xlsx"
all_data = pd.DataFrame()
for f in glob.glob(path+"/*"+file_identifier):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
writer = pd.ExcelWriter('merged_all_sheets.xlsx', engine='xlsxwriter')
all_data.to_excel(writer, sheet_name='Sheet1') 
writer.save()