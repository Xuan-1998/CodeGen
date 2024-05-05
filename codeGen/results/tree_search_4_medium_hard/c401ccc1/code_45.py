import sys

N = 2**30
dp = [False] * N

q = int(sys.stdin.readline())
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    if (u & v) == v and dp[v]:
        print("YES")
    else:
        print("NO")
