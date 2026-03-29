mod = 10**9 + 7
dp = [0] * (5*10**6 + 7)

def f(n):
    if n == 1:
        return 0
    if dp[n]:
        return dp[n]
    res = min(f(n//2) + 1)
    dp[n] = res
    return res

t, l, r = map(int, input().split())
result = sum(t[i]*f(l+i-1) for i in range(r-l+1)) - l*f(r)

print(result % mod)
