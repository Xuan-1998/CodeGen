from functools import lru_cache

@lru_cache(None)
def dp(i):
    if i == 0:
        return 0
    min_cost = float('inf')
    for j in range(1, i+1):
        k = len(s[j-1]) - len(s[i-1])
        min_cost = min(min_cost, dp(j-1) + c[k] + (k == 0 or l[k]))
    return min_cost

n = int(input())
c = [int(input()) for _ in range(n)]
l = [input() for _ in range(n)]

s = [''] * n
for i in range(n):
    s[i] = input()

print(dp(n))
