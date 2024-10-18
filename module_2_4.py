# Дан список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Создаём пустые списки
primes = []  # простых числа
not_primes = []  # не простые числа

# Перебираем все числа из списка numbers
for number in numbers:
    if number == 1:
        continue  # Пропускаем 1, так как она не является ни простым, ни составным числом
    
    is_prime = True  # Проверяем, простое ли число
    
    # Проверяем делители от 2 до number - 1
    for i in range(2, number):
        if number % i == 0:  # Если число делится на i без остатка, значит оно не простое
            is_prime = False
            break  # Прерываем цикл, как только нашли делитель
    
    # Добавляем число в соответствующий список
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

# Выводим списки простых и не простых чисел
print("Primes:", primes)
print("Not Primes:", not_primes)
