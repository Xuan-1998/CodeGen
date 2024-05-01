import heapq

n = int(input())
a = list(map(int, input().split()))
dp = [[0] * 105 for _ in range(105)]

for i in range(n):
    dp[i][a[i]] += 1

for i in range(1, n):
    for j in range(min(a[i-1]-1, a[i]+1), max(-1, a[i]-1)):
        if j > 0:
            dp[i][j] = dp[i-1][j-1]
        elif j < 0:
            dp[i][j] = dp[i-1][j+1]

max_points = 0
for i in range(n):
    max_points += dp[i][a[i]]

print(max_points)
