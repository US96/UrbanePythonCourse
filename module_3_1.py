# Глобальная переменная для подсчета вызовов
calls = 0


# Функция для подсчета вызовов
def count_calls():
    global calls
    calls += 1


# Функция для получения информации о строке
def string_info(string):
    count_calls()  # Увеличиваем счетчик вызовов
    return len(string), string.upper(), string.lower()


# Функция для проверки наличия строки в списке
def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счетчик вызовов
    string_lower = string.lower()
    return any(item.lower() == string_lower for item in list_to_search)


# Пример использования функций
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches

# Вывод количества вызовов функций
print(calls)
