import sys

dp = {i: {} for i in range(10**9+7)}

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        if m == 0:
            print(len(str(n)) % (10**9+7))
        else:
            dp[n][m] = min(dp[d + 1][m - 1] for d in str(n))
            print(dp[n][m])

solve()
