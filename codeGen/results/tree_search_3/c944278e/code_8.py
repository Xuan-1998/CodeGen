import sys

n = int(input())
s = input()

dp = [[0] * (1 << n) for _ in range(n + 1)]
winners = set()

for i in range(1, n + 1):
    for mask in range((1 << i), (1 << (i + 1))):
        j = bin(mask ^ ((1 << i) - 1)).count('1')
        if s[i - 1] == '1':
            dp[i][mask] += dp[i - 1][mask & ~(1 << j)]
        else:
            dp[i][mask] += dp[i - 1][mask & (1 << j)]

for i in range(2 ** n):
    if dp[n][i]:
        winners.add(i)

print(*sorted(list(winners)), sep='\n')
