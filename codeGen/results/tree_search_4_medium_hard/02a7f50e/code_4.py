import sys

# Read input
n = int(input())
dp = [[0] * 1000001 for _ in range(101)]
for _ in range(n):
    a, b = map(int, input().split())

# Fill up the DP table
for i in range(n+1):
    dp[i][0] = i

for j in range(2, 1000001):
    for i in range(j-1, -1, -1):
        if dp[i][j-1] < i + (j // b) + (1 if i > 0 else 0):
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = i

# Calculate the minimum number of beacons that could be destroyed
ans = min(dp[:n])

print(ans)
