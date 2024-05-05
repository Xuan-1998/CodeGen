import sys

# Initialize dp array with False values
n, m = map(int, input().split())
dp = [[False] * (m + 1) for _ in range(n + 1)]

# Read table and initialize dp array
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(m):
        if not dp[i][j]:
            sorted_in_column = all(row[k] <= row[k+1] for k in range(j, m-1))
            dp[i][j] = sorted_in_column

# Read tasks and check if subtable is sorted
k = int(input())
for _ in range(k):
    l, r = map(int, input().split())
    any_sorted = False
    for c in range(m):
        if dp[r][c]:
            any_sorted = True
            break
    print("Yes" if any_sorted else "No")
