import sys

def solution():
    n = int(input())
    k = list(map(int, input().split()))
    h = list(map(int, input().split()))

    dp = [0] * (n + 1)
    j = 0

    for i in range(n):
        while j < n and k[j] <= i:
            j += 1
        if j < n:
            dp[i+1] = min(dp[i], h[j-1]) + 1
        else:
            dp[i+1] = dp[i]

    print(dp[-1])

solution()
