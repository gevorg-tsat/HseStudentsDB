from db import db_start, init_groups, add_group
import ruz
import psycopg2

if __name__ == "__main__":
    db_conn, cursor = db_start()
    init_groups(db_conn=db_conn, cursor=cursor)
    faculties = ruz.utils.get("faculties")
    for fac in faculties:
        groups = ruz.groups(fac['facultyOid'])
        if  len(groups):
            for data in groups:
                data["name"] = data["name"].replace("\'", "").replace('\"','')
                data["number"] = data["number"].replace("\'", "").replace('\"','')
                add_group(db_conn=db_conn, cursor=cursor, data=data)
        else:
            print(f"HMM {fac['facultyOid']}")