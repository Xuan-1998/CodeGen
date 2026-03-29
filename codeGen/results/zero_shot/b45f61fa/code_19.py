n = int(input())
p = list(map(int, input().split()))
dp = [[0] * len(p) for _ in range(len(p))]

for gap in range(2, n):
    for i in range(n - gap):
        j = i + gap
        dp[i][j] = float('inf')
        for k in range(i, j):
            cost = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j+1]
            dp[i][j] = min(dp[i][j], cost)

opt_parentheses = []
for i in range(n - 1):
    min_cost = float('inf')
    for k in range(i, n - 1):
        if dp[i][k] + dp[k+1][n-1] < min_cost:
            min_cost = dp[i][k] + dp[k+1][n-1]
            break
    opt_parentheses.append('(')
    opt_parentheses.append(chr(ord('A') + i))
    opt_parentheses.append(opt_parentheses[:min(k - i + 1, n - k - 2)] + ')')

print(''.join(opt_parentheses))
