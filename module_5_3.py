class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self
    def __radd__(self, value):
        self.number_of_floors = value + self.number_of_floors
        return self
    def __iadd__(self, value):
        self.number_of_floors += value
        return self

house_1 = House('ЖК "Камелот"', 19)
house_2 = House('ЖК "Дворцовый фасад"', 4)

print(house_1)
print(house_2)
print(house_1 == house_2)
house_2 = house_2 + 15
print(house_2)
print(house_1 == house_2)
house_1 += 10
print(house_1)
house_2 = 8 + house_2
print(house_2)
print(house_1 > house_2)
print(house_1 >= house_2)
print(house_1 < house_2)
print(house_1 <= house_2)
print(house_1 != house_2)
