# Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# Часть 1: Вызовы функции с различными аргументами
print_params()  # Вывод: 1 строка True
print_params(10)  # Вывод: 10 строка True
print_params(b=25)  # Вывод: 1 25 True
print_params(c=[1, 2, 3])  # Вывод: 1 строка [1, 2, 3]

# Часть 2: Распаковка списка и словаря
values_list = [100, 'Hello', False]
values_dict = {'a': 200, 'b': 'World', 'c': True}

# Распаковка списка
print_params(*values_list)  # Вывод: 100 Hello False

# Распаковка словаря
print_params(**values_dict)  # Вывод: 200 World True

# Часть 3: Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']

# Распаковываем список и добавляем отдельный параметр
print_params(*values_list_2, 42)  # Вывод: 54.32 Строка 42
