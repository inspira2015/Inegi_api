import csv
from python_mysql import mysql_db
import re


def get_filter_row(row):
    dict_row = {}
    dict_row['id'] = '0'

    for (ind, val) in row.items():
        val = val.replace("'", "\\'")
        if val == '*' or val == '-':
            val = 'null'
        dict_row[ind] = val
    return dict_row


with open("./AGEEML_2023318117180.csv", 'r', encoding="utf8") as csv_file:
    dict_reader = csv.DictReader(csv_file)
    count = 0

    for row in dict_reader:
        if (count > 3):
            break
        
        clean_dict = get_filter_row(row)

        placeholders = ', '.join(['%s'] * len(clean_dict))
        columns = ', '.join(clean_dict.keys())

        list_values = list(clean_dict.values())
        string_values = ', '.join(list_values)
        values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in clean_dict.values())
        values = values.replace( "'null'", 'null')


        sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ("inegi_data", columns, values)


        with mysql_db() as db:
            print(sql)

            print("\n")
            db.execute("INSERT INTO %s ( %s ) VALUES ( %s );" % ("inegi_data", columns, values))
            db.commit()

