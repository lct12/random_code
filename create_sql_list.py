# Write function that turns a normal list into a string representing a SQL list ['a','b','c'] to ('a', 'b', 'c')
def create_sql_list(norm_list,str_list=False,paran_btwn=False):
    # Set str_list = True for lists of strings 
    # Set paran_btwn = True if you want parantheses between elements (rather than just at start and end)
    sql_list = "("
    if str_list == True and paran_btwn==False:
        sql_list += "'"
        sql_list += "','".join(norm_list)
        sql_list += "')"
    elif str_list == False and paran_btwn==False:
        # Must convert to string type to use the sql_list
        norm_list = list(map(str, norm_list))
        sql_list += ",".join(norm_list)
        sql_list += ")"
    elif str_list == True and paran_btwn==True:
        sql_list += "'"
        # join with parantheses between elements
        sql_list += "'),('".join(norm_list)
        sql_list += "')"
    else:
        # Must convert to string type to use the sql_list
        norm_list = list(map(str, norm_list))
        sql_list += "),(".join(norm_list)
        sql_list += ")"
    return sql_list