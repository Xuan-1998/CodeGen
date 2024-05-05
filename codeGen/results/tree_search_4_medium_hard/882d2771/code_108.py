import sys
t, l, r = map(int, input().split())
dp = [[0]*(r+1) for _ in range(l+1)]

for i in range(2):
    for j in range(2, r+1):
        dp[i][j] = 1

for i in range(2, l+1):
    for j in range(2, r+1):
        min_comparisons = sys.maxsize
        for k in range(j+1):
            min_comparisons = min(min_comparisons, dp[i-1][k] + (j-k))
        dp[i][j] = min_comparisons

ans = 0
for i in range(t):
    ans += sum([dp[min(i, l)+1][j] for j in range(min(l, r))])

print(ans % (10**9+7))
