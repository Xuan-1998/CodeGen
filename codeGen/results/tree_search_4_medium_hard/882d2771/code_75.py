def solve(t, l, r):
    memo = {}
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == 0:
            return t[0] * f(j) - j * f(r)
        return min(dp(i-1, k) + t[1] * f(k+1) - k * f(r)) % (10**9 + 7)
    f = [0]
    for i in range(2, l):
        f.append(f[i-1] + 1)
    for i in range(l, r+1):
        f.append(f[i-1] + t[0])
    return dp(r-l+1, l-2) % (10**9 + 7)

# Test the function
t = [1, 2]
l, r = map(int, input().split())
print(solve(t, l, r))
