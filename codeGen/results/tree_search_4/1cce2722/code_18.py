import sys

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    dp = [0] * (n + 1)
    for i in range(n):
        if i > 0:
            dp[i+1] = max(dp[i], dp[n-i-2])
        else:
            dp[1] = max(0, a[0])

    return dp[-1]

print(solve())
