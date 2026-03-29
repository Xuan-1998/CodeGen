dp = {}
def dfs(i, x):
    if i == 0:
        return 1 if x >= ((1 << k) - 1) else 0
    if (i, x) in dp:
        return dp[(i, x)]
    ans = 0
    for j in range(2**k):
        y = j & ((1 << k) - 1)
        z = j ^ ((1 << k) - 1)
        if y >= z and dfs(i-1, z):
            ans += 1
    dp[(i, x)] = ans
    return ans
def solve(n, k):
    ans = 0
    for i in range(n):
        ans += dfs(i, 0)
    return ans % (10**9 + 7)

