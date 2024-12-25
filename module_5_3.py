# module_5_3.py

class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __str__(self):
        return f"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435: {self.name}, \u043a\u043e\u043b-\u0432\u043e \u044d\u0442\u0430\u0436\u0435\u0439: {self.floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.floors <= other.floors
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.floors >= other.floors
        return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.floors != other.floors
        return True

    def __add__(self, value):
        if isinstance(value, int):
            self.floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

# Example usage:
if __name__ == "__main__":
    h1 = House('\u0416\u041a \u042d\u043b\u044c\u0431\u0440\u0443\u0441', 10)
    h2 = House('\u0416\u041a \u0410\u043a\u0430\u0446\u0438\u044f', 20)

    print(h1)
    print(h2)

    print(h1 == h2)  # __eq__

    h1 = h1 + 10  # __add__
    print(h1)
    print(h1 == h2)

    h1 += 10  # __iadd__
    print(h1)

    h2 = 10 + h2  # __radd__
    print(h2)

    print(h1 > h2)  # __gt__
    print(h1 >= h2)  # __ge__
    print(h1 < h2)  # __lt__
    print(h1 <= h2)  # __le__
    print(h1 != h2)  # __ne__
