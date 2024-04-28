n = int(input())
a = list(map(int, input().split()))
dp = [0] * 106
ans = 0

for i in range(1, n+1):
    dp[a[i-1]] = max(dp[a[i-1]], dp[a[i-2]] + (i if a[i-1]%105==0 else 1))
    ans = max(ans, dp[a[i-1]])

print(ans)
