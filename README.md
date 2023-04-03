# random_code
I wrote all the code snippets here to automate things that I frequently do while coding. They can be imported directly into Python if you follow the directions below:

## Background Setup 

If you don't already, make sure you have Anaconda downloaded

### On a Mac
1. Go to your home directory (boaty.mcboatface), then find the path /opt/ananconda3/lib/pythonXX, where XX is the version of Python you have.
2. Create a folder entitled code_snippets in this folder.
3. In this new folder, copy and paste all the Python files downloaded from this GitHub. 
4. Open up Spyder, Jupyter Lab or another Python IDE. To test that everything has been done correctly, run the command from code_snippets import to_excel_multiple_sheets. If nothing happens, congrats! 

### On Windows
1. Go to the file path C:\Users\boaty.mcboatface\Anaconda3\lib where boaty.mcboatface is your user name.
2. Create a folder entitled code_snippets in this folder.
3. In this new folder, copy and paste all the Python files downloaded from this GitHub. 
4. Open up Spyder, Jupyter Lab or another Python IDE. To test that everything has been done correctly, run the command from code_snippets import to_excel_multiple_sheets. If nothing happens, congrats! 

## Description of Python Files
1. `__init__.py` is the central file that pulls all the functions created elsewhere
2. `convertNumbers.py` converts a list containing words and numbers to one that is words and numerals
3. `neuralNetworks.py` trains a Word2Vec neural network on documents that you provide
4. `output_gsheets.py` outputs a pandas dataframe into a google spreadsheet (see below for setup instructions)
5. `preprocess_counter_code.py` preprocesses raw documents (removing stopwords, lemmatisation, etc.) and creates a Counter of the words
6. `return_dict.py` returns a nested dictionary rather than a pandas df to a query 
7. `to_excel_multiple_sheets.py` exports multiple dataframes to the same excel file
8. `sqlUploadDF.py` uses pandas' to_sql function to upload dataframes to SQL
9. `create_sql_list.py` turns a normal list into a string representing a SQL list ['a','b','c'] to ('a', 'b', 'c')


## How to use output_gsheets
This function allows you to output a pandas dataframe object to google sheets.

### Enable the Google Sheets API & set up authorisation.
First, Enable API Access for a Project. To do this, follow the steps below (from [here](https://docs.gspread.org/en/latest/oauth2.html)): 
1. Head to Google Developers Console, and create a new project (or select the one you already have).
2. In the box labeled “Search for APIs and Services”, search for “Google Drive API” and enable it.
3. In the box labeled “Search for APIs and Services”, search for “Google Sheets API” and enable it.

Then, Enable OAuth Client ID by following the following steps (taken from [here](https://docs.gspread.org/en/latest/oauth2.html#oauth-client-id)): 
1. Go to “APIs & Services > OAuth Consent Screen.” Click the button for “Configure Consent Screen”.
2. In the “1 OAuth consent screen” tab, give your app a name and fill the “User support email” and “Developer contact information”, both with your email. Click “SAVE AND CONTINUE”.
3. There is no need to fill in anything in the tab “2 Scopes”, just click “SAVE AND CONTINUE”.
4. In the tab “3 Test users”, add your email. Click “SAVE AND CONTINUE”.
5. Double check the “4 Summary” presented and click “BACK TO DASHBOARD”.
6. Go to “APIs & Services > Credentials”
7. Click “+ Create credentials” at the top, then select “OAuth client ID”.
8. Select “Desktop app”, name the credentials and click “Create”. Click “Ok” in the “OAuth client created” popup.
9. Download the credentials by clicking the Download JSON button in “OAuth 2.0 Client IDs” section.

Finally, download your credentials file and place it in the appropriate location:
1. Once you have downloaded the credentials file in step 6, rename it credentials.json.
2. If you are a Mac User, go to your home directory and click command + shift + . (the period symbol) .This allows you to see hidden files. Find the hidden folder called .config and create a folder in there called gspread. 
3. If you are a Windows User, find the hidden folder %APPDATA%. You should be able to do this by searching %APPDATA% in the File Explorer search bar. Then create a folder entitled gspread. 
4. Move the credentials file created in step 1 to this folder.

### Import relevant packages    
    import pandas as pd
    from code_snippets import output_gsheets

### Create a pandas dataframe
`rawDF = pd.DataFrame({'greetings':['hello','goodbye']})`

### Create a Google Spreadsheet in Google Sheets.
This is where your data will output to, so make sure it's in the correct folder. Find the sheets key (it's the part after https://docs.google.com/spreadsheets/d/...). Copy it.

### Run the output_gsheets command.
The variables to be entered are below. Only raw_df, gsheet_key, and ws_name are mandatory.

1. raw_df = raw pandas dataframe you wish to output
2. gsheet_key = Key to the Google Sheet you are outputting to (found in step 4). Must be a string.
3. ws_name = Name of worksheet you are creating. Must be a string.
4. wrap_cells: Set to True to wrap certain cells in the google sheet
5. cells_wrap: Cells to wrap (for example, enter "D:E" if you want to wrap the text in columns 4 & 5 in the pandas dataframe). Must be a string.
6. resize_columns: Set to True to resize certain cols in google sheet
7. cols_to_resize = Columns to be resized (for example, enter "A:E" if you want to resize the first five columns. Note that you can only resize the width of the column). Must be a string.
8. resize_size: Width size of the columns you are resizing (in pixels)

Example code:

    gSheetKey = '1rvkAMeDylwnWxguQHR_QoeweRyq_ltlp9JngKuYejo4'
    output_gsheets(rawDF,gSheetKey,'test')`

To output multiple sheets, I recommend using a dictionary like so:

    gSheetKey = '1rvkAMeDylwnWxguQHR_QoeweRyq_ltlp9JngKuYejo4'
    dfDict = {'df1': df1, 'df2': df2}

    for wsName, dfName in dfDict.items():
        output_gsheets(dfName,gSheetKey,wsName)
    
The first time you run this command, it launches a browser asking you for authentication. Follow the instruction on the web page. Once finished, gspread stores authorised credentials in the config directory next to credentials.json. You only need to do authorisation in the browser once, as the following runs will reuse stored credentials.





