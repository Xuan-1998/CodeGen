# Input the number of plants (n) and species (m)
n, m = map(int, input().split())
plants = []

# Read the plant information
for i in range(n):
    s, x = map(float, input().split())
    plants.append((s, x))

# Sort the plants by position
plants.sort(key=lambda x: x[1])

dp = [[[0] * (m + 1) for _ in range(m + 1)] for _ in range(m)]

for i in range(1, m + 1):
    dp[i][0][0] = i

for s, x in plants:
    for j in range(1, m + 1):
        if j == s:
            dp[s][j-1][i] += 1
        else:
            min_replanted = float('inf')
            for k in range(m):
                if k != s and dp[k][j-1][i] < min_replanted:
                    min_replanted = dp[k][j-1][i]
            dp[s][j-1][i] += 1 + min_replanted

# Find the minimum number of plants that need to be replanted
min_replanted = float('inf')
for i in range(m):
    if dp[i][m-1][n-1] < min_replanted:
        min_replanted = dp[i][m-1][n-1]

print(min_replanted)
