from sys import stdin

n, k = map(int, stdin.readline().split())
s = stdin.readline().strip()

dp = [""] * (k + 1)
for i in range(k + 1):
    if i == 0:
        dp[i] = ""
    else:
        for j in range(min(i, n)):
            if s[j] == s[k]:
                dp[i] = min(dp[i], dp[i - 1] + s[j])
            elif dp[i].count(s[j]) < k:
                dp[i] = min(dp[i], dp[i - 1] + s[j])

print(dp[-1].ljust(k)[k - 1:])
