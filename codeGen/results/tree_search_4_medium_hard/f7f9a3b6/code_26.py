import sys
from collections import defaultdict

# Read input from stdin
n = int(input())
s = input()
a = [int(x) for x in input().split()]

dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][n] = 1

for i in range(n, -1, -1):
    for j in range(i + 1, n + 1):
        if all(c <= max(a) and c.isalpha() for c in set(s[i:j])):
            dp[i][j] = sum(dp[k][l] for k in range(i, j) for l in range(k + 1, j + 1))
        else:
            dp[i][j] = 0

res = dp[0][n]
print(res % (10 ** 9 + 7))

max_len = max(len(s[i:j]) for i in range(n) for j in range(i + 1, n + 1) if all(c <= max(a) and c.isalpha() for c in set(s[i:j])))
min_substrings = min(1 + (n - i) // len(s[i:j]) for i in range(n) for j in range(i + 1, n + 1) if all(c <= max(a) and c.isalpha() for c in set(s[i:j])))

print(max_len)
print(min_substrings)
