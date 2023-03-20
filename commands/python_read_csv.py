import csv

def get_columns_from_csv_file(filepath):
    with open(filepath, 'r', encoding="utf8") as csv_file:
        dict_reader = csv.DictReader(csv_file)
        dict_csv_reader = dict(list(dict_reader)[0])
    list_of_columns = list(dict_csv_reader.keys())
    return list(map(lambda x: x.upper(), list_of_columns))

