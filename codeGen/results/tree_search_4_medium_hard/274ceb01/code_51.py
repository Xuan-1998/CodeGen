import sys

n = int(input())
marks = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for k in range(i):
        if marks[k] < i:
            dp[i][k+1] = min(dp[j][0] + (i-j)*marks[k] for j in range(k+1)) if k > 0 else None

min_sum = sys.maxsize
for k in range(n, -1, -1):
    if dp[n][k] != 0:
        min_sum = min(min_sum, dp[n][k])
        break

print(min_sum)
