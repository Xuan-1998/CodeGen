import math

def count_odd_factors(n):
    odd_factor_count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if i ** 2 <= n:
            factors = set()
            p = i
            while p <= n:
                if n % p == 0:
                    factors.add(p)
                    if p != i and p * i <= n:
                        factors.add(i)
                p += 1
            if len(factors) % 2 != 0:
                odd_factor_count += 1
    return odd_factor_count

n = int(input())
print(count_odd_factors(n))
