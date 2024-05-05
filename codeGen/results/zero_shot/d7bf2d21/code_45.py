# Read input array
arr = list(map(int, input().split()))

# Initialize variables
n = len(arr)
dp = [[1] * n for _ in range(n)]
max_length = 0

for i in range(n):
    for j in range(i+1):
        if arr[j] < arr[i]:
            dp[i][j] = max(dp[i-1][j-1] if i > 0 else 0, dp[j][i-1] if j > 0 else 0) + 1
            max_length = max(max_length, dp[i][j])

# Calculate the number of longest increasing subsequences
print(sum(1 for row in dp for val in row if val == max_length))
