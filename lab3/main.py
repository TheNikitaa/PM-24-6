from csv_handler import load_table as load_csv, save_table as save_csv
from pickle_handler import load_table as load_pickle, save_table as save_pickle
from table import *

table = Table(headers=['Money', 'Salary', 'Is_work', 'Name', 'Time'])
table.add_row([100, 100, True, 'Alice', datetime.now()])
table.add_row([303, 303, False, 'Nikita', datetime.now()])

save_csv(table, 'data.csv')
load_table_csv = load_csv('data.csv')
load_table_csv.print_table()

save_pickle(table, 'data.pickle')  
load_table_pickle = load_pickle('data.pickle')
with open('data.txt', 'w') as f:
    f.write(str(load_table_pickle))
