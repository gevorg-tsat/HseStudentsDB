import psycopg2

host='127.0.0.1'
login = 'postgres'
password = ''
db_name = 'postgres'

def db_start():
    conn = psycopg2.connect(
        dbname=db_name,
        user=login, 
        password=password,
        host=host
    )
    cursor = conn.cursor()
    return conn, cursor

def init_faculties(db_conn: psycopg2.connection, cursor):
    cursor.execute('CREATE TABLE IF NOT EXISTS faculties(id SERIAL primary key, name TEXT, material TEXT, data_type NUMERIC(1))')
    db_conn.commit()

