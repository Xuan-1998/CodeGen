import math

def odd_divisors(N):
    count = 0
    for i in range(1, N + 1):
        if math.isqrt(i) ** 2 == i:
            count += 1
    return count

N = int(input())
print(odd_divisors(N))
