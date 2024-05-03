import sys

# Read input from stdin
n, m = map(int, input().split())
replanted_plants = [0] * (m + 1)
dp = [[0] * (m + 1) for _ in range(m + 1)]

for i in range(n):
    s, x = map(int, input().split())
    # Update replanted_plants and dp
    if i > 0:
        if replanted_plants[s - 1] == 0:
            replanted_plants[s] = replanted_plants[s - 1]
        else:
            replanted_plants[s] = replanted_plants[s - 1] + 1

        dp[i][s] = min(dp[i][s], replanted_plants[s])

print(min(dp[n]))

