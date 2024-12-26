class House:
    houses_history = []  # Атрибут класса для хранения истории зданий

    def __new__(cls, *args, **kwargs):
        # Добавляем название здания в историю при создании объекта
        if len(args) > 0:  # Проверяем, есть ли переданные аргументы
            cls.houses_history.append(args[0])
        # Создаем объект, вызывая метод __new__ родительского класса
        instance = super().__new__(cls)
        return instance

    def __init__(self, name, floors):
        self.name = name  # Название здания
        self.floors = floors  # Количество этажей

    def __del__(self):
        # Сообщение при удалении объекта
        print(f"{self.name} снесён, но он останется в истории")

# Тестирование
if __name__ == "__main__":
    h1 = House('ЖК Эльбрус', 10)
    print(House.houses_history)  # ['ЖК Эльбрус']

    h2 = House('ЖК Акация', 20)
    print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация']

    h3 = House('ЖК Матрёшки', 20)
    print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

    # Удаление объектов
    del h2
    del h3

    print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
