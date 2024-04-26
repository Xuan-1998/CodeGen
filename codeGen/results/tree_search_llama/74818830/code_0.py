import math

def count_odd_factors(N):
    count = 0
    for i in range(1, int(math.sqrt(N)) + 1):
        if i * i <= N:
            count += 1
    return count

N = int(input())
print(count_odd_factors(N))
