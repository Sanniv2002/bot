import asyncio
import websockets


async def handler(websocket, path):
    try:
        while True:
            print("A Connection Opened")
            data = await websocket.recv()
            print(data)
    except:
        print("A Connection Closed")


async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("Wesocket server running on ws://localhost:8756")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
