p = list(map(int, input().split()))
n = len(p)

dp = [0] * (n + 1)
x = [0] * (n + 1)

for i in range(2, n + 1):
    p_i = p[i - 1]
    x_i = sum(x[:i])
    dp[i] = 1 + (x_i % 2 == 0 ? dp[p_i] : min(dp[j] | p_j < i, j < i))

print(dp[n])  # Output
