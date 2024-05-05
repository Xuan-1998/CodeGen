def f(n):
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = min((dp[j - 1] + j) % (10**9 + 7) for j in range(i - 1))
    return dp[n]

t, l, r = map(int, input().split())
result = sum(t * f(l + i) for i in range(r - l + 1)) - l * f(r)
print(result % (10**9 + 7))
