import csv
from table import Table

def load_table(path):
    with open(path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        data = [r for r in reader]
    return Table(headers, data)

def save_table(table, path):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(table.headers)
        writer.writerows(table.data)
