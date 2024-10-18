#!/usr/bin/env python3
"""Asynchronous coroutine"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous function"""
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
