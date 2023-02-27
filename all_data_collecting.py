import pandas
from db import db_start, get_info
from settings import TABLE_PATH, NEW_TABLE

if __name__ == "__main__":
    db_conn, cursor = db_start()
    table = pandas.read_excel(TABLE_PATH, index_col=0)

    for fio, row in table.iterrows():
        data = get_info(cursor=cursor, fio=fio)
        if len(data) == 0:
            print(fio)
            continue
        qual = ""
        if data[0][1][0] == "С":
            qual = "специалитет"
        elif data[0][1][0] == "Б":
            qual = "бакалавриат"
        elif data[0][1][0] == "М":
            qual = "магистратура"
        table.at[fio,'Программа'] = data[0][1]
        table.at[fio,'Группа'] = data[0][2]
        table.at[fio, 'Квалификация'] = qual
        table.at[fio, 'Курс'] = data[0][3]
    table.to_excel(NEW_TABLE)
