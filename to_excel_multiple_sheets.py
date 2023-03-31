# Create a function that outputs multiple sheets to excel
import os 
import pandas as pd
from os import sep
def to_excel_multiple_sheets(excel_name, sheet_list, df_list,path=''):
    #import pandas as pd
    cwd = os.getcwd()
    if len(sheet_list) != len(df_list):
        return 'Error! Ensure that these two lists have the same # of elements!'
    if path == "":
        path = f'{cwd}{sep}data{sep}'
    writer = pd.ExcelWriter(f"{path}{excel_name}.xlsx",engine="xlsxwriter")
    dfdict = {sheet_list[i]:df_list[i] for i in range(len(sheet_list))}
    for name,df in dfdict.items():
        df.to_excel(writer, sheet_name=name)
    writer.save() 