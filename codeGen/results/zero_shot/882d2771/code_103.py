def f(n):
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = min(dp[j] + j - i for j in range(i))
    return dp[n]

l, r = map(int, input().split())
f_values = [f(i) for i in range(l, r+1)]

t, = map(int, input().split())
expression = sum(t * f_values[i] for i in range(len(f_values)))
expression -= l * f_values[-1]
print(expression % (10**9 + 7))
