import os
import psycopg2

DATABASE_URL = os.environ.get('DATABASE_URL')
db_connection = psycopg2.connect(DATABASE_URL)

