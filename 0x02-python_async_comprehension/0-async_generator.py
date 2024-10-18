#!/usr/bin/env python3
"""A coroutine"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Usign yield in an asynchronus function"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random()

