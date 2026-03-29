import sys

# Read input from stdin
n = int(input())
s = input()
a = list(map(int, input().split()))

# Initialize dp table with zeros
dp = [[0] * 27 for _ in range(n + 1)]
maxWays = [[0] * 27 for _ in range(n + 1)]

dp[0][0] = 1

for i in range(1, n + 1):
    for j in range(26):
        if dp[i-1][j] > 0:
            maxCount = min(a[j], i)
            for k in range(maxCount, -1, -1):
                if sum(s[m] == chr(j+97) for m in range(i-k, i)) <= a[j]:
                    dp[i][j+1] += dp[i-k-1][j]
                    maxWays[i][j+1] += 1

ways = maxWays[n][26]
longestSubstr = 0
minSubstrs = n

for i in range(n):
    for j in range(27):
        if dp[i][j] > 0:
            longestSubstr = max(longestSubstr, i)
            minSubstrs = min(minSubstrs, j)

print((ways % (10**9+7)), (longestSubstr % (10**9+7)), (minSubstrs % (10**9+7)))
