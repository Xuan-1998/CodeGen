import sys

k = int(input())
s = input().strip()

dp = [False] * (k + 1)
dp[0] = True

for i in range(1, k + 1):
    if s[i - 1] <= s[-1]:
        dp[i] = dp[i - 1]
    else:
        dp[i] = dp[i - 1] or dp[i - 2]

ans = ""
i = k
while i > 0:
    if dp[i] and (s[i - 1] <= s[-1] or not dp[i - 1]):
        ans += s[i - 1]
        i -= 1
    elif dp[i - 1]:
        ans += s[i - 2]
        i -= 2
    else:
        break

print(ans)
