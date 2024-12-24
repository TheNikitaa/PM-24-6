from datetime import datetime

class Table:
    def __init__(self, headers=None, data=None):
        self.headers = headers if headers else []
        self.data = data if data else []
        self.column_types = {
            headers[0]: int,
            headers[1]: int,
            headers[2]: bool,
            headers[3]: str,
            headers[4]: datetime,
        }
    def __repr__(self):
        return f'\nHeaders: {self.headers}, \nData: {self.data}'
    
    def print_table(self):
        print("\t".join(self.headers))
        for row in self.data:
            print("\t".join(map(str, row)))

    def add_row(self, row):
        types = [type(el) for el in row]
        for i in range(len(self.headers)):
            if types[i] != self.column_types[self.headers[i]]:
                raise Exception('Ошибка типа данных')
        self.data.append(row)

    def get_rows_by_number(self, start, stop, copy_table=False):
        try:
            rows = self.data[start:stop]
            if copy_table:
                return Table(headers=self.headers, data=rows)
            else:
                return Table(headers=self.headers, data=self.data)
        except Exception as e:
            print('Stop или start должны быть заданы корректно!')

    def get_rows_by_index(self, *args, copy_table=False):
        try:
            filter = [r for r in self.data if r[0] in args]
            if copy_table:
                return Table(headers=self.headers, data=filter)
            else:
                return Table(headers=self.headers, data=self.data)
        except ValueError:
            print('Вы ввели некорректное значение!')

    def set_column_types(self, types_dict, by_number=True):
        if by_number:
            for i, col_type in types_dict.items():
                if i < len(self.headers):
                    self.column_types[self.headers[i]] = col_type
                else:
                    raise IndexError(f'Индекс {i} вышел за границы')
        else:
            for header, col_type in types_dict.items():
                if header in self.headers:
                    self.column_types[header] = col_type
                else:
                    raise KeyError(f'Столбец {header} не найден')
                
    def get_column_types(self, by_number=True):
        if by_number:
            return {i: self.column_types[header] for i, header in enumerate(self.headers)}
        else:
            return self.column_types
        
    def get_values(self, column=0):
        if isinstance(column, int):
            return [r[column] for r in self.data]
        elif isinstance(column, str):
            if column in self.headers:
                col_index = self.headers.index(column)
                return [r[col_index] for r in self.data[:]]
            else:
                raise ValueError(f"Столбец '{column}' не найден в заголовке.")
        else:
            raise TypeError("Колонка должна быть строкой или числом.")
    def get_value(self, column=0):
        if isinstance(column, int):
            return self.data[0][column]
        elif isinstance(column, str):
            if column in self.headers:
                col_index = self.headers.index(column)
                return self.data[0][col_index]
            else:
                raise ValueError(f"Столбец '{column}' не найден в заголовке.")
        else:
            raise TypeError("Колонка должна быть строкой или числом.")
    def set_values(self, values, column=0):
        if isinstance(column, int):
            if column < len(self.headers):
                for i in range(len(values)):
                    self.data[i][column] = values[i]
            else:
                raise IndexError('Индекс колонок вышел за границы.')
        elif isinstance(column, str):
            if column in self.headers:
                col_index = self.headers.index(column)
                for i in range(len(values)):
                    self.data[i][col_index] = values[i]
            else:
                raise ValueError(f"Столбец '{column}' не найден в заголовке.")
        else:
            raise TypeError("Колонка должна быть строкой или числом.")
    def set_value(self, value, column=0):
        if isinstance(column, int):
            if column < len(self.headers):
                self.data[0][column] = value
        elif isinstance(column, str):
            if column in self.headers:
                col_index = self.headers.index(column)
                self.data[0][col_index] = value
            else:
                raise ValueError(f"Столбец '{column}' не найден в заголовке.")
        else:
            raise TypeError("Колонка должна быть строкой или числом.")
    def add(self, column1, column2, name):
        column1_vals = self.get_values(column1)
        column2_vals = self.get_values(column2)
        res = []
        for el1, el2 in zip(column1_vals, column2_vals):
            if isinstance(el1, (int, float)) and isinstance(el2, (int, float)):
                res.append(el1 + el2)
            else:
                raise TypeError("Обе колонки должны быть числами.")
        self.headers.append(name)
        for i in range(len(res)):
            self.data[i].append(res[i])
    def sub(self, column1, column2, name):
        column1_vals = self.get_values(column1)
        column2_vals = self.get_values(column2)
        res = []
        for el1, el2 in zip(column1_vals, column2_vals):
            if isinstance(el1, (int, float)) and isinstance(el2, (int, float)):
                res.append(el1 - el2)
            else:
                raise TypeError("Обе колонки должны быть числами.")
        self.headers.append(name)
        for i in range(len(res)):
            self.data[i].append(res[i])
    def mul(self, column1, column2, name):
        column1_vals = self.get_values(column1)
        column2_vals = self.get_values(column2)
        res = []
        for el1, el2 in zip(column1_vals, column2_vals):
            if isinstance(el1, (int, float)) and isinstance(el2, (int, float)):
                res.append(el1 * el2)
            else:
                raise TypeError("Обе колонки должны быть числами.")
        self.headers.append(name)
        for i in range(len(res)):
            self.data[i].append(res[i])
    def div(self, column1, column2, name):
        column1_vals = self.get_values(column1)
        column2_vals = self.get_values(column2)
        res = []
        for el1, el2 in zip(column1_vals, column2_vals):
            if isinstance(el1, (int, float)) and isinstance(el2, (int, float)):
                if el2 == 0:
                    raise ZeroDivisionError('Вы пытаетесь поделить на 0')
                res.append(el1 / el2)
            else:
                raise TypeError("Обе колонки должны быть числами.")
        self.headers.append(name)
        for i in range(len(res)):
            self.data[i].append(res[i])
    def eq(self, column1, column2):
        column1_vals = self.get_values(column1)
        column2_vals = self.get_values(column2)
        return [v1 == v2 for v1, v2 in zip(column1_vals, column2_vals)]
    def gr(self, column1, column2):
        column1_vals = self.get_values(column1)
        column2_vals = self.get_values(column2)
        return [v1 > v2 for v1, v2 in zip(column1_vals, column2_vals)]
    def ls(self, column1, column2):
        column1_vals = self.get_values(column1)
        column2_vals = self.get_values(column2)
        return [v1 < v2 for v1, v2 in zip(column1_vals, column2_vals)]
    def ge(self, column1, column2):
        column1_vals = self.get_values(column1)
        column2_vals = self.get_values(column2)
        return [v1 >= v2 for v1, v2 in zip(column1_vals, column2_vals)]
    def le(self, column1, column2):
        column1_vals = self.get_values(column1)
        column2_vals = self.get_values(column2)
        return [v1 <= v2 for v1, v2 in zip(column1_vals, column2_vals)]
    def ne(self, column1, column2):
        column1_vals = self.get_values(column1)
        column2_vals = self.get_values(column2)
        return [v1 != v2 for v1, v2 in zip(column1_vals, column2_vals)]
    def filter_rows(self, bool_list, copy_table=False):
        if len(bool_list) != len(self.data):
            raise ValueError("Число строк не совпадает с исходным количеством.")
        filtred_data = []
        for i in range(len(self.data)):
            if bool_list[i]:
                filtred_data.append(self.data[i])
        if copy_table:
            return Table(headers=self.headers, data=filtred_data)
        else:
            return Table(headers=self.headers, data=self.data)
