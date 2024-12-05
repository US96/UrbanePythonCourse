# Создание класса House
class House:
    # Метод __init__ для инициализации объекта
    def __init__(self, name, number_of_floors):
        self.name = name  # Название дома
        self.number_of_floors = number_of_floors  # Количество этажей

    # Метод для перемещения на указанный этаж
    def go_to(self, new_floor):
        # Проверка на допустимость этажа
        if 1 <= new_floor <= self.number_of_floors:
            # Вывод номеров этажей от 1 до new_floor
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")


# Создание объектов класса House
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# Вызов метода go_to для объекта h1
h1.go_to(5)
print("---")
# Вызов метода go_to для объекта h2
h2.go_to(10)
