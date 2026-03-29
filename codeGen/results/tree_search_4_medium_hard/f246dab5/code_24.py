from math import inf

n = int(input())
dp = [inf] * 10**9
dp[0] = dp[1] = 50
for i in range(n):
    t = int(input())
    j = max(j for j in range(t) if dp[j] < inf)
    dp[t] = min(dp[j-1], dp[j]) + (t-j)*20
print(*dp, sep='\n')
