# Write function that returns a nested dictionary to a query rather than a pandas df 
def return_dict(query, conn):
    # Conn = connection to database of choice
    cursor = conn.cursor(as_dict=True)
    cursor.execute(query)
    my_query = cursor.fetchall()
    return {i:my_query[i] for i in range(len(my_query))}

     