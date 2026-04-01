import asyncio
from pywb import WBClient


async def main():
    token = "your_api_token_here"

    async with WBClient(token) as client:
        result = await client.ping()
        print(f"TS: {result.ts}, Status: {result.status}")


if __name__ == "__main__":
    asyncio.run(main())
