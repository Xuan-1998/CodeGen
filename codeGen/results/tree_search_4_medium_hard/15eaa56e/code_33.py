import sys

n, m = map(int, input().split())
table = []
for _ in range(n):
    row = list(map(int, input().split()))
    table.append(row)

k = int(input())
tasks = []
for _ in range(k):
    l, r = map(int, input().split())
    tasks.append((l, r))

# Create a dynamic programming array
dp = [[False] * m for _ in range(m)]

# Iterate over all columns and check if sorted
for j in range(m):
    max_val = -sys.maxsize
    for i in range(n):
        max_val = max(max_val, table[i][j])
        dp[j][j] = (table[i][j] <= max_val)
        for col in range(j-1, -1, -1):
            if not dp[col][j]:
                break
            if table[i][col] > table[i][j]:
                dp[j][j] = False
                break

# Check if any column has at least one "True"
sorted_in_at_least_one_column = False
for col in range(m):
    for row in range(n):
        if row < n - 1 and table[row][col] <= table[row+1][col]:
            sorted_in_at_least_one_column = True
            break

print("Yes" if sorted_in_at_least_one_column else "No")
