# https://projecteuler.net/problem=2

def fibonacci_generator() -> (int, int):
    a = 1
    b = 2
    index = 0
    while True:
        yield a, index
        a, b = b, a + b
        index += 1

def fibonacci(n: int) -> (int, int):
    gen = fibonacci_generator()
    result = gen.__next__()
    while(result[1] < n):
        result = gen.__next__()
    return result

def sum_even_fibonacci_below(val: int) -> int:
    gen = fibonacci_generator()
    sum = 0
    result = gen.__next__()
    while(result[0] < val):
        if(result[0] % 2 == 0):
            sum += result[0]
        result = gen.__next__()
    return sum


