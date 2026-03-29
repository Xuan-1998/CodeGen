def f(n):
    if n in dp:
        return dp[n]
    if n == 0:  # base case
        return 0
    res = 0
    for i in range(len(t)):
        res += t[i] * f((n - 1) // (i + 1))
    res -= (n - 1) * f(n - 1)
    dp[n] = res % (10**9 + 7)
    return res

t, l, r = map(int, input().split())
dp = {}
print(f(r))  # call the function with the desired range
