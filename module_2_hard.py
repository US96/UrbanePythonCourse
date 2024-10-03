def find_password(n):
    password = ''  # Пустая строка для хранения результата

    # Перебираем все возможные пары чисел от 1 до n
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:  # Проверяем кратность числа n сумме пары
                password += str(i) + str(
                    j)  # Добавляем пару в строку результата

    return password


# Пример использования:
n = int(input("Введите число от 3 до 20: "))
print(f"Нужный пароль: {find_password(n)}")
