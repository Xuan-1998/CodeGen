import sys

n = int(sys.stdin.readline())
p = [int(x) for x in sys.stdin.readline().split()]

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n):
    for j in range(i+1, n):
        dp[i][j] = min(dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j] for k in range(i, j))

result = []
i, j = 1, n-1
while i < j:
    k = j - (j-i)//2
    result.append('(')
    if k > i: result.append('A' + str(k))
    if j > k: result.append('B' + str(j))
    result.append(')')
    i, j = k+1, j-1

print(''.join(result) + ')')
