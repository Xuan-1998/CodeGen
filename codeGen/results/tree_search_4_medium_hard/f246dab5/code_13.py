from sys import stdin

n = int(stdin.readline())
dp = [0]*1000001
dp[0] = 20
dp[1] = min(20, 50)

for i in range(2, n+1):
    t_i = int(stdin.readline())
    if t_i > 90:
        dp[i] = min(dp[i-1], dp[i-2]) + 50
    else:
        dp[i] = min(dp[i-1], dp[i-2]) + 20

print(sum(dp))
