from sys import stdin

n = int(stdin.readline())
arr = [int(x) for x in stdin.readline().split()]

dp = [[1] * n for _ in range(n)]

for i in range(1, n):
    for j in range(n):
        if arr[i] > arr[j]:
            dp[i][j] = max(dp[i-1][k] + 1 for k in range(j) if arr[k] < arr[i])

max_length = max(max(row) for row in dp)
print(max_length)
