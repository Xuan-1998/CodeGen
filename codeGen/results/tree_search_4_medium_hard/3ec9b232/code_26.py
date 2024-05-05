import sys
from math import factorial
from functools import lru_cache

@lru_cache(None)
def count_permutations(arr):
    n = len(arr)
    total_permutations = 1
    for num in arr:
        total_permutations *= factorial(n - 1) // (factorial(num - 1) if num > 0 else 1)
        n -= 1
    return total_permutations

n = int(input())
m = list(map(int, input().split()))

dp = [{} for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(i):
        if m[i - 1] <= j:
            dp[i][j] = (dp.get((i - 1), {}).get(j, 0) or 0) + count_permutations(m[:i])
        else:
            dp[i][j] = dp[i - 1].get(j, 0)

print(dp[-1].get(n - 1, 0))
