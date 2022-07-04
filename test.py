import random
import asyncio

async def main():
    i = 1
    while i < 2:
        a = random.randint(1,1000)
        print(a)
        await asyncio.sleep(3)

asyncio.run(main())