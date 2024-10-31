class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
house_1 = House('ЖК "Камелот"', 19)
house_2 = House('ЖК "Дворцовый фасад"', 4)
print(house_1)
print(house_2)
print(len(house_1))
print(len(house_2))
