import sys

# Read input from standard input
n, m = map(int, input().split())
dp = [[False] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    col_sorted = True
    prev_val = row[0]
    for j in range(1, m + 1):
        if row[j] < prev_val:
            dp[i][j] = True
            break
        prev_val = row[j]

# Process tasks
k = int(input())
for _ in range(k):
    l, r = map(int, input().split())
    for j in range(1, m + 1):
        if all(dp[i][j] for i in range(l - 1, r)):
            print("Yes")
            break
    else:
        print("No")

