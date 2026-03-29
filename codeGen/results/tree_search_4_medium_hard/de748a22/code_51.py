code_block
n, q = map(int, input().split())
signs = list(input())

dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    dp[i][i] = sum(1 if signs[j] == '+' else -1 for j in range(i, i + 1))
for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + abs(sum(1 if signs[l] == '+' else -1 for l in range(k, j))))
dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    dp[0][i] = sum(1 if signs[j] == '+' else -1 for j in range(i, n))
for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[k][j] + abs(sum(1 if signs[l] == '+' else -1 for l in range(k, n))))
for _ in range(q):
    l, r = map(int, input().split())
    print(min(abs(sum(1 if signs[j] == '+' else -1 for j in range(l, r)))))

