import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    delay = 12 / power
    number = 1
    for _ in range(5):
        await asyncio.sleep(delay)
        print(f'Силач {name} поднял {number} шар')
        number += 1
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Миша', 2))
    task2 = asyncio.create_task(start_strongman('Гриша', 3))
    task3 = asyncio.create_task(start_strongman('Коля', 4))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())
