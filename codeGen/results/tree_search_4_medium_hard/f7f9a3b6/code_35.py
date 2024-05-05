import sys
from math import comb

n = int(input())
s = input()
a = [int(x) for x in input().split()]

dp = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]

for i in range(1, n + 1):
    for j in range(i):
        if a[ord(s[j])-97] > 1:
            dp[i][j] = sum((k == 0 and 1 or dp[i-k][0]) * comb(i-k-1, a[ord(s[i-k-1])-97]-1) for k in range(1, i+1))
        else:
            dp[i][j] = 1

print(dp[-1][-1])
longest_substring_length = max(range(len(s)), key=lambda x: dp[n][x])
print(longest_substring_length)
min_substrings = min(range(len(s)), key=lambda x: dp[n][x])
print(min_substrings + 1)
