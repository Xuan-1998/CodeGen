# Read the input
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

# Initialize a table to store the maximum joy for each hare
dp = [[0]*3 for _ in range(n)]

# Fill up the table
for i in range(n):
    if i == 0:
        dp[i][1] = c[0]
    elif i == n-1:
        dp[i][2] = a[-1]
    else:
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + b[i]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + c[i]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + a[i]

# Print the maximum joy
print(max(max(row) for row in dp))
