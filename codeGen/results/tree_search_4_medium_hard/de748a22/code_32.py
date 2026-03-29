code
from collections import defaultdict

n, q = map(int, input().split())
signs = [1 if x == '+' else -1 for x in input()]

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i):
        dp[i][j] = min(dp[k-1][i-1] + signs[k-1] for k in range(j+1))

ans = []
for _ in range(q):
    l, r = map(int, input().split())
    ans.append(min(dp[l-1][r-1]))

print('\n'.join(map(str, ans)))
