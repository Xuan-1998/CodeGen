import math

def count_odd_divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if (i ** 2) <= n:
            count += 1
    return count

n = int(input())
print(count_odd_divisors(n))
