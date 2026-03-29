import sys

n = int(input())
s = input()
a = list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(26):
        if s[i - 1].ord() - ord('a') == j and dp[i - a[j]] > 0:
            dp[i] = max(dp[i], dp[i - a[j]] + 1)

print((dp[-1] % (10**9 + 7)))

max_length = 0
for i in range(n, -1, -1):
    if dp[i] > 0 and (i == n or s[i - 1].ord() - ord('a') != s[i].ord() - ord('a')):
        max_length = i + 1
        break

print(max_length)

min_substrings = -(-n // min(a))
print(min_substrings)
