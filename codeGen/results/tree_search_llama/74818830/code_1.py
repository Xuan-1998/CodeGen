import math

def count_odd_factors(n):
    count = 0
    i = 1
    while i * i <= n:
        count += 1
        i += 1
    return count

n = int(input())
print(count_odd_factors(n))
