# Определяем функцию get_multiplied_digits
def get_multiplied_digits(number):
    # Преобразуем число в строку для работы с отдельными цифрами
    str_number = str(number)

    # Извлекаем первую цифру числа и преобразуем её обратно в число
    first = int(str_number[0])

    # Базовый случай: если длина строки равна 1, возвращаем первую цифру
    if len(str_number) == 1:
        return first

    # Рекурсивный случай: умножаем первую цифру на результат функции с остальными цифрами
    return first * get_multiplied_digits(int(str_number[1:]))


# Пример использования функции
result = get_multiplied_digits(40203)

# Выводим результат
print(result)  # Ожидаемый вывод: 24
