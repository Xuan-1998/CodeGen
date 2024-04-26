import math

def count_odd_factor_numbers(n):
    count = 0
    for i in range(1, n + 1):
        factors = set()
        p = i
        while p > 1:
            for j in range(2, int(math.sqrt(p)) + 1):
                if p % j == 0:
                    factors.add(j)
                    p //= j
                    break
            else:
                factors.add(p)
                break
        sqrt_i = math.isqrt(i)
        if sqrt_i * sqrt_i == i:
            count += 1
    return count

n = int(input())
print(count_odd_factor_numbers(n))
