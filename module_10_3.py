import threading
from time import sleep
from random import randint

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            replenishment = randint(50, 500)
            self.balance += replenishment
            print(f'Пополнение: {replenishment}. Баланс: {self.balance}.\n', end = '')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(100):
            withdrawal = randint(50, 500)
            print(f'Запрос на {withdrawal}.\n', end = '')
            if withdrawal <= self.balance:
                self.balance -= withdrawal
                print(f'Снятие: {withdrawal}. Баланс: {self.balance}.\n', end = '')
            else:
                print('Запрос отклонён, недостаточно средств.\n', end = '')
                self.lock.acquire()
            sleep(0.001)

bk = Bank()

th1 = threading.Thread(target = Bank.deposit, args = (bk, ))
th2 = threading.Thread(target = Bank.take, args = (bk, ))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}.')


