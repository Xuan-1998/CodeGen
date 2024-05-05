import sys

q = int(input())
dp = [False]*2**30

for _ in range(q):
    u, v = map(int, input().split())
    for x in range(2**30):
        if (u & x) == x:
            dp[x] = True
    print('YES' if dp[v] else 'NO')
