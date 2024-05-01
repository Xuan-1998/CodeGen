import sys
from collections import defaultdict

N = int(input())
dp = [[0]*N for _ in range(N)]

str1 = input()
str2 = input()

memo = defaultdict(int)

def get_dp(i, j):
    if memo.get((i, j)):
        return memo[(i, j)]
    if i == 0 or j == 0:
        return 0
    if str1[i] == str2[j]:
        dp[i][j] = 1 + get_dp(i-1, j-1)
    else:
        dp[i][j] = max(get_dp(i-1, j), get_dp(i, j-1))
    memo[(i, j)] = dp[i][j]
    return dp[i][j]

result = 0
for i in range(N):
    for j in range(N):
        result = max(result, get_dp(i, j))

print(result)
