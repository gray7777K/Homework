class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)
house_1 = House('ЖК "Камелот"', 19)
house_2 = House('ЖК "Дворцовый фасад"', 4)

house_1.go_to(4)
house_1.go_to(20)
house_2.go_to(3)
house_2.go_to(0)
