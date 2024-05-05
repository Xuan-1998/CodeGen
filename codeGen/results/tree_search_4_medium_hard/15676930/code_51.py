import sys

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i == 1:
            dp[i] = a[0]
        elif i == 2:
            dp[i] = max(a[0], b[0])
        else:
            dp[i] = max(dp[i-1], dp[i-2] + c[i-2])
    return dp[-1]

print(solve())
