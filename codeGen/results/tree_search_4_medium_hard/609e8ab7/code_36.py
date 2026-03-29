import sys
from collections import deque

# Read input
n = int(input())
p = list(map(int, input().split()))
l = []
r = []
for i in range(1, n):
    l.append(tuple(map(int, input().split())))
    r.append(tuple(map(int, input().split())))

# Initialize DP table
dp = [[float('inf')] * (10**9 + 1) for _ in range(n)]

# Process vertices in topological order
q = deque([(n - 1, l[n - 2], r[n - 2]))]

while q:
    i, li, ri = q.popleft()
    dp[i][ri[0]] = min(dp[i][li[0]] + (ri[0] - li[0]) // 2, dp[i][ri[1]] + (ri[1] - li[1]) // 2)
    for j in range(1, i):
        if p[j] == i:
            q.append((j, l[j - 1], r[j - 1]))
            break
dp[1][r[0][1]]

# Print the minimum number of operations needed
print(min(dp[1]))
