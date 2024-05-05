import sys

n = int(input())
s = input()
a = [int(x) for x in input().split()]

dp = [[0] * 27 for _ in range(n + 1)]
min_substrs = float('inf')
longest_substring = 0

for i in range(2, n + 1):
    for j in range(1, min(i // a[ord(s[i-1]) - 1] + 1, 27)):
        if s[i-1] not in s[:i-1]:
            dp[i][j] = min(dp[i-1][k-1] + 1 for k in range(j))
        else:
            dp[i][j] = dp[i-1][j]
    dp[i][0] = dp[i-1][0]

min_substrs = min(min(dp[n]))
longest_substring = max(x for x in dp[n])

print((dp[n].index(min_substrs)) % (10**9 + 7))
print(longest_substring)
print(min_substrs)
