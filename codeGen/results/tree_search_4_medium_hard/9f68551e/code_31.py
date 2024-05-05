import sys

def solve():
    n = int(input())
    k = list(map(int, input().split()))
    h = list(map(int, input().split()))

    dp = {i: 0 for i in range(n)}
    dp[0] = h[0]

    for i in range(1, n):
        dp[i] = min(dp[i-1], k[i]) + (h[i] - 1) // 1 if dp[i-1] >= h[i] else dp[i-1]
    print(dp[-1])

solve()
