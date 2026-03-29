import sys
from collections import defaultdict

n = int(input())
s = input()
a = [int(x) for x in input().split()]

dp = [[0] * (n + 1) for _ in range(n + 1)]
longest_substring = 0
min_substrings = float('inf')

for i in range(1, n + 1):
    for j in range(i, n + 1):
        if all(c <= a[ord(c) - ord('a')] for c in set(s[i-1:j])):
            dp[i][j] = 1
            longest_substring = max(longest_substring, j - i + 1)
            min_substrings = min(min_substrings, j - i + 1)

count = dp[0][n]
for i in range(1, n):
    if s[i-1] not in [chr(x) for x in range(ord('a'), ord('z')+1)]:
        continue
    count += dp[i][n]

print(count % (10**9 + 7))
print(longest_substring)
print(min_substrings)
