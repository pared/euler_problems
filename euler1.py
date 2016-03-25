# https://projecteuler.net/problem=1

def sum_3_5_multilpiers_below_generator():
    '''int -> int'''
    sum = 0
    index = 0
    while True:
        yield sum, index
        if index % 3 == 0 or index % 5 == 0:
            sum += index
        index += 1


def sum_3_5_multipliers_below(n: int) -> int:
    gen = sum_3_5_multilpiers_below_generator()
    pair = gen.__next__()
    while pair[1] < n:
        pair = gen.__next__()
    return pair[0]


