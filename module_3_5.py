def get_multiplied_digits(number):
    # Преобразуем число в строку для работы с отдельными цифрами
    str_number = str(number)

    # Базовый случай: если длина строки равна 1, возвращаем первую цифру
    if len(str_number) == 1:
        # Если это 0, возвращаем 1, чтобы не умножать на 0
        return int(str_number) if str_number != '0' else 1

    # Извлекаем первую цифру числа и преобразуем её обратно в число
    first = int(str_number[0])

    # Если первая цифра равна 0, пропускаем её и продолжаем с остальными цифрами
    if first == 0:
        return get_multiplied_digits(int(str_number[1:]))

    # Рекурсивный случай: умножаем первую цифру на результат функции с остальными цифрами
    return first * get_multiplied_digits(int(str_number[1:]))

# Пример использования функции
result = get_multiplied_digits(40203)

# Выводим результат
print(result)  # Ожидаемый вывод: 24

# Дополнительная проверка для числа с нулями в конце
result_with_zeros = get_multiplied_digits(40200)
print(result_with_zeros)  # Ожидаемый вывод: 8
