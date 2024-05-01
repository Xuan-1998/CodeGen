===BEGIN CODE===
from itertools import zip_longest
N = int(input())
str1, str2 = input().split() for _ in range(2)
dp1 = [[0] * (N+1) for _ in range(N+1)]
dp2 = [[0] * (N+1) for _ in range(N+1)]

for i in range(N+1):
    dp1[i][0] = 1
    dp2[0][i] = 1

max_len = 0
for i, c1 in enumerate(str1):
    for j, c2 in zip_longest(str2, fillvalue='#'):
        if c1 == c2:
            dp2[i+1][j+1] = dp1[i][j]
            max_len = max(max_len, i + 1)

print(max_len)
===END CODE===
