import sys

n = int(input())
s = input()
a = [int(x) for x in input().split()]

freq = [0] * 26
for c in s:
    freq[ord(c) - ord('a')] += 1

dp = [[0] * (n + 1) for _ in range(n + 1)]

max_len = 0
min_count = n
ans = 0

for i in range(1, n + 1):
    for j in range(i, n + 1):
        if freq[ord(s[j - 1]) - ord('a')] > a[ord(s[j - 1]) - ord('a')]:
            dp[i][j] = 0
        else:
            if i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i - 1][j - 1] + 1) % (10 ** 9 + 7)
        max_len = max(max_len, j - i + 1)
        min_count = min(min_count, dp[i][j])

print(dp[n][n] % (10 ** 9 + 7))
print(max_len)
print(min_count)
