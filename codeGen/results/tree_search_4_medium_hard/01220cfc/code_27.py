import sys

def canReach(arr):
    n = len(arr)
    dp = [False] * n
    dp[0] = True
    for i in range(1, n):
        if not dp[i]:
            for j in range(i - 1, -1, -1):
                if arr[j] >= i - j and (j == 0 or dp[j]):
                    dp[i] = True
                    break
        else:
            continue
    return dp[-1]

# Read input from stdin
arr = list(map(int, input().split()))

# Print the answer to stdout
print(canReach(arr))
