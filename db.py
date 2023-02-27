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
    print("db connected")
    cursor = conn.cursor()
    return conn, cursor

def init_faculties(db_conn, cursor):
    cursor.execute('CREATE TABLE IF NOT EXISTS \
                   faculties(Oid NUMERIC(5) primary key, \
                   Gid NUMERIC(5), name TEXT, UID TEXT, \
                   institute TEXT, abbr VARCHAR(30), code VARCHAR(30))')
    db_conn.commit()

def add_facultie(db_conn, cursor, data: dict):
    cursor.execute('INSERT INTO faculties (Oid, Gid, name, UID, institute, abbr, code)' \
                   "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (data['facultyOid'], data['facultyGid'],
                    data['name'], data['facultyUID'], data['institute'], data['abbr'], data['code']))
    db_conn.commit()

def init_groups(db_conn, cursor):
    cursor.execute('CREATE TABLE IF NOT EXISTS \
                   groups(Oid NUMERIC(10) primary key, \
                   Gid NUMERIC(10), name TEXT, short_name TEXT, course NUMERIC(1), \
                   UID TEXT, faculty NUMERIC(5), \
                   kindEducation int, speciality TEXT, YearOfEducation int, \
                   FOREIGN KEY (faculty) REFERENCES faculties(Oid))')
    db_conn.commit()

def add_group(db_conn, cursor, data: dict):
    command = "INSERT INTO groups (Oid, Gid, name, short_name, course, UID, faculty, kindEducation, speciality, YearOfEducation) VALUES"
    command += f"""({data['groupOid']}, {data['groupGid']}, '{data['name']}', '{data['number']}', {data['course']}, """
    command += f"'{data['groupUID']}', {data['facultyOid']}, {data['kindEducation']}, '{data['speciality']}', {data['YearOfEducation']})"
    
    try :
        cursor.execute(command)
        db_conn.commit()
    except Exception:
        print(data)
        exit()

def init_students(db_conn, cursor):
    cursor.execute('CREATE TABLE IF NOT EXISTS \
                   students(Oid NUMERIC(12) primary key, \
                   Gid NUMERIC(10), fio TEXT, grp NUMERIC(10) REFERENCES groups(Oid))')
    db_conn.commit()

def add_student(db_conn, cursor, data: dict, group):
    command = f"INSERT INTO students (Oid, Gid, fio, grp) VALUES({data['studentOid']}, {data['studentGid']}, '{data['fio']}', {group})"
    cursor.execute(command)
    db_conn.commit()


def get_groups(cursor):
    cursor.execute("SELECT Oid from groups")
    return cursor.fetchall()