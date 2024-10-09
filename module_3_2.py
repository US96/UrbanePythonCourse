def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# 1. Вызовы с разным количеством аргументов
print_params()                    # 1, строка, True
print_params(b=25)                # 1, 25, True
print_params(c=[1, 2, 3])         # 1, строка, [1, 2, 3]
print_params(10, 'example', False)  # 10, example, False

# 2. Распаковка параметров из списка и словаря
values_list = [42, "Hello", False]
values_dict = {'a': 100, 'b': 'Test', 'c': [7, 8, 9]}

print_params(*values_list)         # 42, Hello, False
print_params(**values_dict)        # 100, Test, [7, 8, 9]

# 3. Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)   # 54.32, Строка, 42
