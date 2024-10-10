first = int(input("Введите 1-е число: "))
second = int(input("Введите 2-е число: "))
third = int(input("Введите 3-е число: "))
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
