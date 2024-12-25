class House:
    def __init__(self, name, floors):
        """
        Инициализация объекта дома.
        :param name: Название дома
        :param floors: Количество этажей
        """
        self.name = name
        self.floors = floors

    def __str__(self):
        """
        Возвращает строковое представление объекта.
        """
        return f"Название: {self.name}, кол-во этажей: {self.floors}"

    # Перегрузка оператора сравнения ==
    def __eq__(self, other):
        """
        Проверяет равенство этажей.
        :param other: Объект для сравнения
        """
        return isinstance(other, House) and self.floors == other.floors

    # Перегрузка оператора <
    def __lt__(self, other):
        """
        Проверяет, меньше ли количество этажей.
        :param other: Объект для сравнения
        """
        return isinstance(other, House) and self.floors < other.floors

    # Перегрузка оператора <=
    def __le__(self, other):
        """
        Проверяет, меньше или равно количество этажей.
        :param other: Объект для сравнения
        """
        return isinstance(other, House) and self.floors <= other.floors

    # Перегрузка оператора >
    def __gt__(self, other):
        """
        Проверяет, больше ли количество этажей.
        :param other: Объект для сравнения
        """
        return isinstance(other, House) and self.floors > other.floors

    # Перегрузка оператора >=
    def __ge__(self, other):
        """
        Проверяет, больше или равно количество этажей.
        :param other: Объект для сравнения
        """
        return isinstance(other, House) and self.floors >= other.floors

    # Перегрузка оператора !=
    def __ne__(self, other):
        """
        Проверяет неравенство этажей.
        :param other: Объект для сравнения
        """
        return not self.__eq__(other)

    # Перегрузка оператора +
    def __add__(self, value):
        """
        Увеличивает количество этажей на указанное значение.
        :param value: Количество этажей для добавления
        """
        if isinstance(value, int):
            self.floors += value
        return self

    # Перегрузка оператора +, когда объект находится справа
    def __radd__(self, value):
        """
        Обрабатывает добавление, когда число слева, а объект справа.
        :param value: Количество этажей для добавления
        """
        return self.__add__(value)

    # Перегрузка оператора +=
    def __iadd__(self, value):
        """
        Обрабатывает добавление для оператора +=.
        :param value: Количество этажей для добавления
        """
        return self.__add__(value)


# Пример использования
if __name__ == "__main__":
    # Создаем два дома
    h1 = House('ЖК Эльбрус', 10)
    h2 = House('ЖК Акация', 20)

    # Вывод информации о домах
    print(h1)
    print(h2)

    # Сравнение домов по количеству этажей
    print(h1 == h2)  # Равны ли этажи

    # Добавление этажей к первому дому
    h1 = h1 + 10  # Увеличиваем этажи на 10
    print(h1)
    print(h1 == h2)  # Сравниваем снова

    # Использование оператора +=
    h1 += 10
    print(h1)

    # Использование оператора +, когда число слева
    h2 = 10 + h2
    print(h2)

    # Сравнения домов
    print(h1 > h2)  # h1 больше h2?
    print(h1 >= h2)  # h1 больше или равен h2?
    print(h1 < h2)  # h1 меньше h2?
    print(h1 <= h2)  # h1 меньше или равен h2?
    print(h1 != h2)  # h1 не равен h2?
