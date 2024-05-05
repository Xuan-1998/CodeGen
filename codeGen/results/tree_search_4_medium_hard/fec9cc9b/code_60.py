from collections import defaultdict

n, m = map(int, input().split())
a = list(map(int, input().split()))

dp = defaultdict(lambda:defaultdict(str))
dp[0][0] = 0
dp[0][1] = 0

for i in range(1, n+1):
    dp[i][0] = max(dp[k][0] for k in range(1, i+1) if (a[k-1] <= a[k]) or ((i-k)>0 and dp[k-1][1]>0))  
    dp[i][1] = max(dp[k][1] for k in range(1, i+1) if (a[k-1] >= a[k]) or ((i-k)>0 and dp[k-1][0]>0))  

for _ in range(m):
    l, r = map(int, input().split())
    print("Yes" if dp[r][0] > 0 and dp[l-1][1] == 0 else "No")
