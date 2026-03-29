import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

dp = [[0] * (n + 1) for _ in range(n)]
for i in range(1, n):
    dp[i][i] = 0
for L in range(2, n + 1):
    for i in range(1, n - L + 2):
        j = i + L - 1
        dp[i][j] = sys.maxsize
        for k in range(i, j):
            cost = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[i] * p[j]
            if cost < dp[i][j]:
                dp[i][j] = cost

order = []
i, j = 0, n - 1
while i < j:
    min_cost = sys.maxsize
    k = i
    for k in range(i, j):
        if dp[i][k] + dp[k + 1][j] <= min_cost:
            min_cost = dp[i][k] + dp[k + 1][j]
            k_split = k
    order.append((i, k_split))
    i = k_split + 1
    j = k_split

print(''.join(f'({{"A" + str(i) if i else "A"}}, {{"A" + str(j) for j in range(i, n)}})') for i, j in order)
