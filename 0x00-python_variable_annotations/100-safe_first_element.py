#!/usr/bin/env python3
'''Augment the following code'''


from typing import Any, Optional, Iterable


def safe_first_element(lst: Iterable[Any]) -> Optional[Any]:
    '''return first element or none'''
    if lst:
        return next(iter(lst))
    else:
        return None
