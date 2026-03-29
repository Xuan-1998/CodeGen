import sys

n, k = map(int, input().split())
s = input()

dp = [['' for _ in range(n+1)] for _ in range(k+1)]

for len in range(1, k+1):
    for idx in range(n-len+1):
        if len == 1:
            dp[len][idx] = s[idx]
        else:
            if s[idx+len-1] <= s[idx]:
                dp[len][idx] = min(dp[len-1][idx], s[idx+len-1]+dp[len-1][idx+len-1])
            else:
                dp[len][idx] = min(s[idx+len-2]+dp[len-1][idx], dp[len-1][idx+len-1])

print(min(dp[k]))
