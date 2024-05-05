import sys

n = int(input())
s = input()
a = [int(x) for x in input().split()]

dp = [[0] * (n + 1) for _ in range(26)]
for i in range(26):
    dp[i][0] = 1
for c in s:
    i = ord(c) - ord('a')
    if not dp[i][0]:
        continue
    for j in range(n, 0, -1):
        if j <= a[i]:
            break
        dp[i][j] += min(dp[i][j-a[i]], 1)
        if j == n:
            break
print((dp[0][n]) % (10**9 + 7))

max_length = max(j for i in range(26) for j in range(n+1) if dp[i][j])
min_substrings = min(j for i in range(26) for j in range(n+1) if dp[i][j] == dp[0][n])

print(max_length)
print(min_substrings)
