import os
import psycopg2

DATABASE_URL = os.environ.get('TEST_DATABASE_URL')
db_connection = psycopg2.connect(DATABASE_URL)

def fetch_tuples(query):
    cursor = db_connection.cursor()
    cursor.execute(query)
    tuples = cursor.fetchall()
    cursor.close()
    return tuples
