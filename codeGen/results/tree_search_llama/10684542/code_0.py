import math

def get_exponent(n, p):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)

    exponents = [0] * len(factors)
    for i, factor in enumerate(factors):
        exponent = 0
        while n % (p ** exponent) == 0:
            exponent += 1
        exponents[i] = exponent - 1

    max_exponent = max(x for x in exponents if x >= math.log(n, p))
    return max_exponent if max_exponent is not None else None
