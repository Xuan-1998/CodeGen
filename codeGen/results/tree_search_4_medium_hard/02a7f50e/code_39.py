import sys

# Read input from stdin
n = int(input())
dp = [[0] * n for _ in range(n)]
pos, power = [], []

for _ in range(n):
    a, b = map(int, input().split())
    pos.append(a)
    power.append(b)

pos.sort(reverse=True)

# Initialize the base case
for j in range(n):
    dp[0][j] = 0

# Fill up the dynamic programming array
for i in range(1, n):
    for j in range(i):
        if pos[j] + power[j] > pos[i]:
            dp[i][j] = min(dp[i-1][k] + 1 for k in range(j))
        else:
            dp[i][j] = dp[i-1][j]

# The minimum number of beacons that could be destroyed is stored in the last cell
print(min(dp[-1]))

