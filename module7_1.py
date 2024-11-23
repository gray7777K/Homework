import os

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r', encoding = 'utf-8') as file:
            return file.read()

    def add(self, *products):
        name = self.__file_name
        for i in products:
            if not os.path.isfile(self.__file_name):
                file = open(name, 'w', encoding = 'utf-8')
                file.write(f'{str(i)}\n')
            else:
                if i.name and str(i.weight) in self.get_products():
                    print(f'Продукт {i.__str__()} уже есть в магазине')
                    continue
                else:
                    file = open(name, 'a', encoding = 'utf-8')
                    file.write(f'{str(i)}\n')
            file.close()

shop1 = Shop()

product1 = Product('Огурцы', 0.5, 'Овощи/фрукты')
product2 = Product('Гречка ядрица', 0.9, 'Бакалея')
product3 = Product('Перчатки резиновые', 0.1, 'Промтовары')

print(product2)

shop1.add(product1, product2, product3)

print(shop1.get_products())







