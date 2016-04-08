# https://projecteuler.net/problem=3


def all_factors(n: int) -> int:
    factors =[]
    currentval = n
    i = 2
    while i <= int(currentval):
        if currentval % i == 0:
            factors.append(i)
            currentval /= i
        else:
            i += 1
    return factors

print (max(all_factors(600851475143)))




