import sys

n, k = map(int, input().split())
s = input()

dp = {0: ''}

for i in range(1, k+1):
    if i == 1:
        dp[i] = s[0]
    else:
        for j in range(i-2, -1, -1):
            if (len(dp[j]) + 1) <= i and dp[j][-1] <= s[-1]:
                dp[i] = dp[j] + s[-1]
                break
        else:
            # If no duplication is possible, delete the last character
            dp[i] = dp[i-1][:-1]

print(dp[k])
