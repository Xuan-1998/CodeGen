import sys

def canReach(arr):
    n = len(arr)
    dp = [False] * (n + 1)

    dp[0] = True

    for i in range(1, n):
        if arr[i - 1] >= i - j and dp[j]:
            dp[i] = True
        j -= 1

    return dp[-1]

# Read input from stdin
arr = list(map(int, input().split()))

# Print the result to stdout
print(canReach(arr))
