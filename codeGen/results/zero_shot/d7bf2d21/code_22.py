import sys

def longest_increasing_subsequences(arr):
    n = len(arr)
    dp = {i: 1 for i in range(n)}
    max_length = 1
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        max_length = max(max_length, dp[i])
    return sum(1 for x in dp.values() if x == max_length)

# Read input from stdin
arr = list(map(int, sys.stdin.readline().split()))

# Print the answer to stdout
print(longest_increasing_subsequences(arr))
