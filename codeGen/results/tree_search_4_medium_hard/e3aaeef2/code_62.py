import math

dp = [[0] * (200005) for _ in range(1000005)]
MOD = 10**9 + 7

def solve():
    n, m = map(int, input().split())
    print(dp[n][m]%MOD)

for i in range(n+1):
    dp[i][0] = 0
    for j in range(1, min(i,m)+1):
        if j == 1:
            dp[i][j] = math.ceil(math.log10(i))
        else:
            dp[i][j] = min(dp[k][j-1] + math.ceil(math.log10(i)) - math.log10(k) for k in range(1,i+1))

solve()
