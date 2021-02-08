import asyncio
import websockets

async def hello(country):
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")
async def bye():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")
CMD=input()
if(CMD == "hello"):
    asyncio.get_event_loop().run_until_complete(hello("TW"))
else:
    asyncio.get_event_loop().run_until_complete(bye())