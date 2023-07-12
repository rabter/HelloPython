from time import perf_counter
import requests
import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor

def test_asyncio(self):
    async def get_products(i: int):
        async with aiohttp.ClientSession() as session:
            url = f"https://localhost/product/products"
            async with session.get(url) as response:
                print(i)
                return await response.text()

    async def get_requests():
        coro_list = [get_products(i) for i in range(10)]
        response_list = await asyncio.gather(*coro_list) # unpacking

    stime = perf_counter()
    asyncio.run(get_requests())
    print(f"elapsed time: {perf_counter() - stime:.2f} seconds")
    # elapsed time: 4.16 seconds
def test_syncio(self):
    response_list = []

    def get_products():
        for i in range(10):
            url = f"https://localhost/product/products"
            response = requests.get(url)
            response_list.append(response.text)
            print(i)

    stime = perf_counter()
    get_products()
    print(f"elapsed time: {perf_counter() - stime:.2f} seconds")
    # elapsed time: 5.88 seconds

def test_multithread(self):
    def get_product(i: int):
        url = f"https://localhost/product/products"
        response = requests.get(url)
        print(i)
        return response.text
    def get_products():
        with ThreadPoolExecutor(max_workers=10) as exe:
            futures = [exe.submit(get_product, i) for i in range(10)]
            response_list = [future.result() for future in futures]

    stime = perf_counter()
    get_products()
    print(f"elapsed time: {perf_counter() - stime:.2f} seconds")
    # elapsed time: 4.48 seconds
