""" Рабочие методы 1-7 """


"""get_rows_by_number(start, [stop], copy_table=False)"""
# res = table.get_rows_by_number(1, 2, copy_table=True)  works
# print(res)

"""get_rows_by_index(val1, … , copy_table=False)"""
# new_table_view = table.get_rows_by_index(1, 2, copy_table=True)  works
# print("\nПредставление таблицы:")
# print(new_table_view)

"""set_column_types(types_dict, by_number=True)"""
# # Задание типов столбцов по именам
# types_dict_by_name = {'Id': int, 'Salary': str, 'Is_work': int, 'Name': float}
# table.set_column_types(types_dict_by_name, by_number=False)

# print(table)

# # Задание типов столбцов по индексам
# types_dict_by_index = {0: int, 1: str, 2: int, 3: float}
# table.set_column_types(types_dict_by_index, by_number=True)

# print(table)

"""get_column_types(by_number=True)"""
# Получение типов столбцов по именам
# column_types_by_name = table.get_column_types(by_number=False)

# print("Типы столбцов по именам:", column_types_by_name)

# # Получение типов столбцов по индексам
# column_types_by_index = table.get_column_types(by_number=True)

# print("Типы столбцов по индексам:", column_types_by_index)

"""get_values(column=0)"""
# print(table.get_values(column='Name'))

"""get_value(column=0)"""
# print(table.get_value(column='Name'))

"""set_values(value, column=0)"""
# table.set_values(['Bob', 'Donald'], column="Name")

"""set_values(value, column=0)"""
# table.set_value(10101.3, column=1)

"""print_table()"""
# table.print_table()

"""Реализация таска 6 на два балла"""
# table.add(column1='Salary', column2='Money', name='Sum')
# table.sub(column1='Salary', column2='Money', name='Sub')
# table.mul(column1='Salary', column2='Money', name='Mul')
# table.div(column1='Salary', column2='Money', name='Div')

"""Реализация 7 таска на три балла"""
# e = table.eq('Money', 'Salary')
# e = table.gr('Money', 'Salary')
# e = table.ls('Money', 'Salary')
# e = table.ge('Money', 'Salary')
# e = table.le('Money', 'Salary')
# e = table.ne('Money', 'Salary')
# new_table = table.filter_rows(e, copy_table=True)
# new_table.print_table()

"""Реализация таска 5 на два балла"""
# ~Описана в коде~
