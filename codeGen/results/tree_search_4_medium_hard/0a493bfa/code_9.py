import math

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dp = [[-math.inf for _ in range(m+1)] for _ in range(n+1)]

    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def f(s):
        p = min((p for p in range(2, int(math.sqrt(s))+1) if s%p == 0), default=s)
        if p not in b: return f(s//p) + s
        else: return f(s//p) - s

    dp[0][0] = f(reduce(gcd, a))
    for i in range(1, n+1):
        for j in range(m+1):
            if j < m and b[j] <= i:
                for k in range(i-1, -1, -1):
                    dp[i][j] = max(dp[i][j], dp[k][j-1] * f(reduce(gcd, a[k+1:i+1])) + (i-b[j]) * a[b[j]])
            else: 
                if i == 0: continue
                dp[i][j] = max(dp[:i].index(max(x for x in dp[:i] if x >= 0)) or 0, key=lambda k: dp[k][0])
    return max(max(dp[n], default=-math.inf))

print(solve())
