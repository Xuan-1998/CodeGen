from functools import lru_cache

@lru_cache(None)
def even_odd_sum(n):
    return sum(int(digit) for digit in str(n)) // 2 if all(int(digit) % 2 == 0 for digit in str(n)) else sum(1 for digit in str(n) if int(digit) % 2 != 0)

@lru_cache(None)
def diamonds(i, j):
    return abs(even_odd_sum(i + j - 1) - even_odd_sum(j))

n = int(input())
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] += diamonds(i, j)

print(sum(dp[i][i] for i in range(1, n + 1)))
