import gspread

import df2gspread as d2g
import matplotlib.pyplot as plt
from gspread_dataframe import set_with_dataframe
from gspread_formatting import *


def output_gsheets(raw_df, gsheet_key, ws_name, wrap_cells=False,
		cells_wrap="A:E", resize_columns=False, cols_to_resize="D:E", resize_size=100):
    '''
    This formula outputs a dataframe to Google Sheets
    raw_df = raw dataframe we are drawing from 
    gsheet_key = Key to the Google Sheet we are outputting to
    ws_name = Name of worksheet we are creating
    wrap_cells: Set to True to wrap certain cells in the google sheet
    cells_wrap: Cells to wrap
    resize_columns: Set to True to resize certain cols in google sheet
    cols_to_resize = Columns to be resized 
    resize_size: Resizing size of columns (in pixels)
    Note: to run this code, you will need to follow the instructions on this page: https://docs.gspread.org/en/latest/oauth2.html
    '''
    # Export to Google Sheets

    gc = gspread.oauth()

    # Google spreadsheet
    sh = gc.open_by_key(gsheet_key)

    # Add a sheet and fill it in
    # If sheet already exists will throw an API error - then assign worksheet as worksheet_name 
    try:
        worksheet = sh.add_worksheet(title=ws_name, rows=f"{len(raw_df)}", cols=f"{raw_df.shape[1]}")
    except:
        worksheet = sh.worksheet(ws_name)

    worksheet.clear()
    # Wrap cells (if necessary) and resize columns
    if wrap_cells==True:
        worksheet.format(cells_wrap, {"wrapStrategy": "WRAP"})
    if resize_columns==True:
        set_column_width(worksheet, cols_to_resize, resize_size)
    set_with_dataframe(worksheet, raw_df) 



