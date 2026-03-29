dp = [[-1 for _ in range(109+7)] for _ in range(5*10**6 + 1)]

def solve(n, k):
    if n == 0: return 0
    if k > l: return dp[n][k-1] + k - l

    if dp[n][k] == -1:
        res = 1
        for i in range(2, k+1): res = min(res, solve(n-1, i))
        dp[n][k] = res + 1
    return dp[n][k]

t, l, r = map(int, input().split())
res = 0
for i in range(l, r+1):
    res += solve(t-i-1, i+l)
print((res - l*solve(0, r)) % (10**9 + 7))
