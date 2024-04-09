import os
import psycopg2

if os.environ.get('ENVIRONMENT') == "PRODUCTION":
    db_connection = psycopg2.connect(os.environ.get('DATABASE_URL')
if os.environ.get('ENVIRONMENT') == "TESTING":
    db_connection = psycopg2.connect(dbname=os.environ.get('TEST_DATABASE_NAME'), user=os.environ.get('DATABASE_USERNAME'), password=os.environ.get('DATABASE_PASSWORD'), host=os.environ.get('DATABASE_HOST'), port=os.environ.get('DATABASE_PORT'))


def fetch_tuples(query):
    cursor = db_connection.cursor()
    cursor.execute(query)
    tuples = cursor.fetchall()
    cursor.close()
    return tuples
