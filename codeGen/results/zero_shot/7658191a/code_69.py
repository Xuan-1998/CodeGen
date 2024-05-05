import sys

def max_score(n, k, z, arr):
    dp = [0] * (k + 1)
    for i in range(1, n+1):
        for j in range(min(i, k), -1, -1):
            if j <= z:
                dp[j] = max(dp[j], dp[j-1] + arr[i-1])
            else:
                dp[j] = max(dp[j], dp[j-1] + arr[i-1], dp[j-2] + arr[i-1])
    return dp[k]

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_score(n, k, z, arr))
