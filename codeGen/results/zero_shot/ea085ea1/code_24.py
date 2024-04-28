import sys
from collections import defaultdict

N = int(sys.stdin.readline())
str1 = list(sys.stdin.readline().strip())
str2 = list(sys.stdin.readline().strip())

dp1, dp2 = [0] * (N + 1), [0] * (N + 1)
for i in range(N):
    if str1[i] == str2[i]:
        dp1[i + 1] = dp1[i] + 1
        dp2[i + 1] = dp2[i] + 1

ans, res = 0, [0]
for i in range(N):
    for j in range(i + 1, N):
        if str1[i:i + j + 1] == str2[:j + 1]:
            if dp1[j] - dp2[j] > ans:
                ans = dp1[j] - dp2[j]
print(ans)
