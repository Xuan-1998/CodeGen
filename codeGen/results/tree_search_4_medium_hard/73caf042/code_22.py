from functools import lru_cache

@lru_cache(None)
def f(i, j):
    n = i + j - 1
    even_sum = sum(int(digit) for digit in str(n) if int(digit) % 2 == 0)
    odd_sum = sum(int(digit) for digit in str(n) if int(digit) % 2 != 0)
    return abs(even_sum - odd_sum)

T = int(input())
for _ in range(T):
    N = int(input())
    total_diamonds = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            total_diamonds += f(i, j)
    print(total_diamonds)
