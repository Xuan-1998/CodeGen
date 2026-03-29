import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [0] * (m + 1)
        dp[0] = 1
        for i in range(1, m + 1):
            if 2 * i > n:
                dp[i] = n * dp[i-1]
            else:
                dp[i] = n * dp[2*i - 1]
        print(dp[m] % (10**9 + 7))

solve()
