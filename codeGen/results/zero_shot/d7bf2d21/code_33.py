import sys

# Read the input from stdin
n = int(input())
arr = list(map(int, input().split()))

# Initialize dp and max_length
dp = [1] * n
max_length = 0

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    max_length = max(max_length, dp[i])

# Print the result to stdout
print(max_length)
