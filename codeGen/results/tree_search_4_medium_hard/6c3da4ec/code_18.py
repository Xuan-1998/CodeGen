===BEGIN SOLUTION===
from itertools import combinations
n = int(input())
s = input()

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    dp[i][i+1] = s[i]

max_or = 0

# compute bitwise OR of all possible pairs of non-empty substrings
for k in range(2, n+1):
    for i, j in combinations(range(n), k):
        a = int(''.join(s[i:j+1]), 2)
        b = int(''.join(s[j:n]), 2)
        dp[i][j] = max(dp[i][j], a | b)

print(bin(max(dp[0][-1]))[2:])
