import asyncio


async def func():
    print("Hello!")
    await asyncio.sleep(2)  # Pause for 2 second without blocking
    await asyncio.sleep(2)  # Pause for 2 second without blocking
    await asyncio.sleep(2)  # Pause for 2 second without blocking
    print("Geeks for Geeks")  #


asyncio.run(func())
