#!/usr/bin/env python3
'''Annotate the below function'''


from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Annotate function'''
    return [(i, len(i)) for i in lst]
