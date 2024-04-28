import sys
from collections import defaultdict

N = int(sys.stdin.readline())
str1, str2 = sys.stdin.readline().strip(), sys.stdin.readline().strip()

dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

max_length = 0
for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            max_length = max(max_length, dp[i][j])

print(max_length)
