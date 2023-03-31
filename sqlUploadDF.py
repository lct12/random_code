# This function uses panda's to_sql function to upload dataframes to SQL
import math
import pandas
import yaml
import os
from os import sep


def uploadDF(df,tableName,tableSchema,if_exists='append',con=conn):
    # df = df to be uploaded
    # tableName = name of table
    # tableSchema = name of schema to put table in
    # con = connection to be uploaded to
    
    # Can only upload 1000 records at a time :o
    numLoops = math.ceil(len(df)/1000)
    for loop in range(numLoops):
        toUpload = df[loop*1000:(loop+1)*1000]
        toUpload.to_sql(name = f'{tableName}', schema = f'{tableSchema}', 
            con=con, if_exists=if_exists, index=False, method='multi')
        # Print every 10,000 to keep track of progress
        if loop%10 == 0 and loop != numLoops-1:
            print(f'{(loop+1)*1000} records done!')
    print('All done!')