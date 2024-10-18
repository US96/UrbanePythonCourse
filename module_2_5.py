def get_matrix(n, m, value):
    # 'n' — количество строк (внешних списков).
    # 'm' — количество столбцов (внутренних списков).
    # 'value' — значение, которым будут заполнены все ячейки матрицы.
    # Если будет передано отрицательное значение или 0, то возвращается пустой список
    if n <= 0 or m <= 0:
        return []

    matrix = []  # создаем пустую матрицу

    for i in range(n):  # создаём цикл по строкам
        row = []  # создаем пустую строку

        for j in range(m):  # цикл по столбцам
            row.append(value)  # добавляем значение в строку

        matrix.append(row)  # добавляем строку в матрицу

    return matrix  # возвращаем готовую матрицу

# Вызов функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)
