import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнование.')
    for i in range(5):
        await asyncio.sleep(power)
        print(f'Силач {name} поднял {i + 1}-й шар.')

    print(f'Силач {name} закончил соревнование.')


async def start_tournament():
    strongman1 = asyncio.create_task(start_strongman('Саша', 3))
    strongman2 = asyncio.create_task(start_strongman('Миша', 4))
    strongman3 = asyncio.create_task(start_strongman('Петя', 5))

    await strongman1
    await strongman2
    await strongman3


if __name__ == '__main__':
    asyncio.run(start_tournament())
