def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызов вложенной функции
    inner_function()


# Вызов функции test_function
test_function()

# Попытка вызвать вложенную функцию
# вне test_function inner_function()
# вызовет ошибку NameError
