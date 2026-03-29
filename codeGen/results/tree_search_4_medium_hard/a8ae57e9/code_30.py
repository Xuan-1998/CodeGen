from sys import stdin

dp = [[0 for _ in range(1001)] for _ in range(1002)]

n, k, r = map(int, stdin.readline().split())
for i in range(n):
    c, p = map(int, stdin.readline().split())

k -= 1
r -= 1

for i in range(k+1):
    dp[i][0] = 0
for j in range(1001):
    dp[0][j] = 0

for i in range(1, k+1):
    for j in range(1, 1001):
        if j < c*r:
            dp[i][j] = max(dp[i-1][j], 0)
        else:
            dp[i][j] = max(dp[i-1][j-c*r] + p, dp[i][j-c])

max_earnings = dp[k][r]
accepted_requests = 0
total_amount = 0

i = k
j = r
while i > 0 and j > 0:
    if dp[i][j] != dp[i-1][j]:
        accepted_requests += 1
        total_amount += p
        j -= c*r
    i -= 1

print(accepted_requests, total_amount)

for i in range(accepted_requests):
    print(i+1, (r+1)//c)
