def calculate_structure_sum(data):
    total = 0  # Шаг 2: Инициализируем счетчик
    
    for item in data:  # Шаг 3: Цикл для обхода элементов
        if isinstance(item, (int, float)):  # Шаг 4: Проверка на число
            total += item
        elif isinstance(item, str):  # Проверка на строку
            total += len(item)
        elif isinstance(item, (list, tuple, set)):  # Проверка на список, кортеж или множество
            total += calculate_structure_sum(item)  # Рекурсивный вызов
        elif isinstance(item, dict):  # Проверка на словарь
            for key, value in item.items():  # Обход ключей и значений
                if isinstance(key, (int, float)):
                    total += key
                elif isinstance(key, str):
                    total += len(key)
                if isinstance(value, (int, float)):
                    total += value
                elif isinstance(value, str):
                    total += len(value)
                elif isinstance(value, (list, tuple, set)):
                    total += calculate_structure_sum(value)
    
    return total  # Шаг 5: Возвращаем результат

# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # Ожидаемый вывод: 99
