import sys

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]
dp = [[0] * (max(arr) + 1) for _ in range(n)]

for i, val in enumerate(arr):
    for j in range(val - 1, -1, -1):
        dp[i][j] = max(dp[i][j], dp[i-1].get(j, 0)) if i > 0 else 1

max_length = max(max(row) for row in dp)
print(sum(1 for row in dp if max(row) == max_length))
