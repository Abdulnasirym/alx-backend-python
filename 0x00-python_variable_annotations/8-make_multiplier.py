#!/usr/bin/env python3
'''annotated function'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''return multiply'''
    def multiply(num: float) -> float:
        '''return num(float) * multiplier(float)'''
        return num * multiplier
    return multiply
