from main import db_connection

def fetch_tuples(query):
    cursor = db_connection.cursor()
    cursor.execute(query)
    tuples = cursor.fetchall()
    cursor.close()
    return tuples