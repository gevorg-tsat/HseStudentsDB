from db import db_start, init_faculties, add_facultie
import ruz

if __name__ == "__main__":
    db_conn, cursor = db_start()
    init_faculties(db_conn=db_conn, cursor=cursor)
    info = ruz.utils.get("faculties")
    #info = json.loads(info)
    for data in info:
        add_facultie(db_conn=db_conn, cursor=cursor, data=data)
    