import sys

def lis_count(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# Read input from stdin
arr = list(map(int, sys.stdin.readline().split()))

# Calculate the number of longest increasing subsequences
count = lis_count(arr)

# Print the result to stdout
print(count)
