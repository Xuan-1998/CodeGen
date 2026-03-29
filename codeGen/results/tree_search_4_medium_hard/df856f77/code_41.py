import sys

def min_operations(arr):
    n = len(arr)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n):
        j = i - 1
        while j >= 0 and arr[j] >= arr[i]:
            j -= 1
        if j < 0:
            dp[i] = 1 + (dp[i-1] if i > 0 else 0)
        else:
            dp[i] = 1 + dp[j]

    return dp[-1]

# Input and output handling
n = int(input())
arr = list(map(int, input().split()))
print(min_operations(arr))
