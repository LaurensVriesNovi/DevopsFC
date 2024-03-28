import os
import psycopg2

db_connection = psycopg2.connect(
    database=os.getenv("POSTGRES_URL"),
)
