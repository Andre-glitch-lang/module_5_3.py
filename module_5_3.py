class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(0, new_floor + 1):          # а по заданию надо поставить вместо 0 (или убрать) => 1
            if 1 <= new_floor <= self.number_of_floors:
                print(i)
                continue
            if 0 == new_floor:
                print(f'Это подвал или парковка на нижнем этаже: {new_floor}')
                continue
            else:
                print(f'Такого этажа не существует: {new_floor}')
                break

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

# дополнено методами:
    def __eq__(self, other):                                                            # 1
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __add__(self, value):                                                           # 3
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __iadd__(self, value):                                                          # 3
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):                                                          # 2
        return self.__iadd__(value)   # или заменим условием (все три строчки следующие) или __add__
        # if isinstance(value, int):
        #     self.number_of_floors += value
        # return self

    def __gt__(self, other):                                                            # 2
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):                                                            # 2
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):                                                            # 2
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):                                                            # 2
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):                                                            # 2
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)

h1 = h1 + 10
print(h1)
print(h1 == h2)

h1 += 10
print(h1)

h2 = 10 + h2
print(h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)     