import sys

dp = [0]*100000
dp2 = [sum(range(i+1)) for i in range(100000)]
a = [int(x) for x in input().split()]

ans = 0
for i in range(len(a)):
    if a[i] == 0:
        ans += dp[i-1]
    else:
        for j in range(i):
            if a[i]%j == 0 and (j == 0 or a[i]%j == 0):
                ans += dp[j-1]*dp2[i-j]

print(ans%1000000007)
