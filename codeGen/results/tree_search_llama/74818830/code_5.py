import math

def count_odd_factors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % (i ** 2) == 0:
            count += 1
    return count

n = int(input())
print(count_odd_factors(n))
