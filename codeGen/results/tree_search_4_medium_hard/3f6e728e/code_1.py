import sys
from collections import defaultdict

dp = defaultdict(int)
C = int(input())

for _ in range(C):
    N, M = map(int, input().split())
    upper = list(map(int, input().split()))
    lower = list(map(int, input().split()))

    for r in set(upper):
        dp[r] += 1
    for r in set(lower):
        dp[r] -= 1

print(*[v % (10**9 + 7) for v in dp.values()], sep=' ')
