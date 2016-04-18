import copy
from functools import reduce


def get_factors(n: int) -> list:
    factors = [1]
    factor = 2
    current_value = n
    while factor <= current_value:
        if current_value % factor == 0:
            factors.append(factor)
            current_value /= factor
        else:
            factor += 1
    return factors


def smallest_number_divided_by_numbers(start: int, end: int) -> int:
    index = start
    result = []
    while index <= end:
        factors = get_factors(index)
        result.extend(list_difference(result, factors))
        yield reduce(lambda x, y: x*y, result)
        index += 1


def list_difference(l1: list, l2: list) -> list:
    copy1 = copy.copy(l1)
    copy2 = copy.copy(l2)

    for value in copy1:
        if value in copy2:
            copy2.remove(value)

    return copy2


