#!/usr/bin/env python3
"""A function that takes an integer"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """A function identical to wait_n"""
    wait_times = await asyncio.gather(
        *(task_wait_random(max_delay) for _ in range(n))
    )
    return sorted(wait_times)
