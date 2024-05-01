# Read the input sequence and number of elements
n = int(input())
a = list(map(int, input().split()))

# Initialize the dp table with 0s for all k values
dp = [[0] * (n+1) for _ in range(n+1)]

# Fill up the dp table using dynamic programming
for i in range(1, n+1):
    for k in range(min(i, n), -1, -1):
        if a[i-1] == a[k-1] + 1 or a[i-1] == a[k-1] - 1:
            dp[i][k] = max(dp[i-1][k-1], dp[i-1][k])
        else:
            dp[i][k] = dp[i-1][k]

# Return the maximum points that can be earned
print(max(dp[n]))
