import psycopg2

db_connection = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="password",
    host="localhost",  # Of het IP-adres van je databasehost
    port="5432"  # De standaard PostgreSQL-poort
)