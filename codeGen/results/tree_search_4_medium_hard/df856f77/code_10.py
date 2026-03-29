===BEGIN SOLUTION===
import sys

def min_operations(arr):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(n):
        dp[i + 1] = dp[i]
        for j in range(i):
            if arr[j] <= arr[i]:
                dp[i + 1] = min(dp[i + 1], dp[j] + (arr[i] - arr[j]))

    return dp[-1]

n = int(input())
arr = list(map(int, input().split()))
print(min_operations(arr))
