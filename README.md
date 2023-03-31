# random_code
I wrote all the code snippets here to automate things that I frequently do while coding. They can be imported directly into Python if you follow the directions below:

## Background Setup (this is assuming you have Jupyter Lab downloaded on your computer)

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
5. `preprocess_counter_code.py` preprocesses raw documents (removing stopwords, lemmatisation, etc.) and creates a counter of the words
6. `return_dict.py` returns a nested dictionary to a query rather than a pandas df


## Setup to use 
