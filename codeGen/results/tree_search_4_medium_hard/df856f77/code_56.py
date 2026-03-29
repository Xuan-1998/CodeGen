import sys

def min_operations(arr):
    n = len(arr)
    dp = [0] * n
    for i in range(1, n):
        dp[i] = min(dp[i-1], 1 + abs(arr[i] - min(arr[i+1:])))
    return dp[-1]

n = int(input())
arr = list(map(int, input().split()))
print(min_operations(arr))
