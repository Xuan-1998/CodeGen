===BEGIN CODE===
from collections import defaultdict

N = int(input())
dp = [[0] * N for _ in range(N)]

preStr1 = [0] * (N + 1)
for i in range(N):
    preStr1[i + 1] = preStr1[i]
    for j in range(i, -1, -1):
        if str1[i] == str2[j]:
            preStr1[i + 1] = max(preStr1[i + 1], preStr1[j] + 1)

preStr2 = [0] * (N + 1)
for i in range(N):
    preStr2[i + 1] = preStr2[i]
    for j in range(i, -1, -1):
        if str2[i] == str1[j]:
            preStr2[i + 1] = max(preStr2[i + 1], preStr2[j] + 1)

for i in range(N):
    for j in range(N):
        if str1[i] != str2[j]:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        else:
            dp[i][j] = 1 + dp[i - 1][j - 1]

print(max(map(max, dp)))
===END CODE===
