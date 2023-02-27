from db import db_start, init_students, add_student, get_groups
import ruz

if __name__ == "__main__":
    db_conn, cursor = db_start()
    init_students(db_conn=db_conn, cursor=cursor)
    groups = get_groups(cursor)
    for group in groups:
        groupOid = int(group[0])
        students = ruz.staff_of_group(group_id=groupOid)
        if students:
            for stud in students:
                add_student(db_conn=db_conn, cursor=cursor, data=stud, group=groupOid)
        else:
            print(f"HMM {groupOid}")
    