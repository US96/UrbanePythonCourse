def generate_password(n):
    result = ""
    # Цикл для перебора всех возможных пар чисел
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            # Если сумма пары делится на n без остатка
            if (i + j) % n == 0:
                result += f"{i}{j}"  # Добавляем пару к результату
    return result
n = int(input("Введите число от 3 до 20: "))
print(generate_password(n))
