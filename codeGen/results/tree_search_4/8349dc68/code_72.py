# Read the input array and k
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

# Initialize dp table
dp = [[0] * (k + 1) for _ in range(n + 1)]

# Fill up the dp table
for i in range(1, n + 1):
    for j in range(1, min(i, k) + 1):
        if j == 1:
            dp[i][j] = max(arr[:i])
        else:
            dp[i][j] = max(dp[i-1][j], arr[i-j])

# Initialize the maximum sum
max_sum = 0

# Iterate over the partitions and calculate the sums
for i in range(k, n + 1):
    for j in range(1, k + 1):
        if i >= j:
            max_sum = max(max_sum, dp[i][j])

print(max_sum)
