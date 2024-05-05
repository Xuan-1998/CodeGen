import sys

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [[False] * (n + 1) for _ in range(n)]

    for i in range(n):
        dp[i][1] = True

    for j in range(2, n + 1):
        for i in range(j - 1, -1, -1):
            if arr[i] < arr[j - 1]:
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = max(dp[k][j - 1] for k in range(i) if arr[k] < arr[j - 1])

    max_length = 0
    for i in range(n):
        for j in range(1, n + 1):
            if dp[i][j]:
                max_length = j
                break

    return max_length

# Read input from stdin
arr = [int(x) for x in sys.stdin.readline().split()]

# Print the answer to stdout
print(longest_increasing_subsequence(arr))
