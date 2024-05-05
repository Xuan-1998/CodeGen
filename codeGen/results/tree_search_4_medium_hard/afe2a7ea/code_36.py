import sys

def comb(n, k):
    res = 1
    for i in range(k):
        res = (res * (n - i)) // (i + 1)
    return res

def solve():
    n = int(sys.stdin.readline().strip())
    dp = [0] * (n + 2)
    dp[0] = comb(n + 1, 0) % 998244353
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] * comb(n, i) % 998244353
    return (dp[n] * pow(2, n, 998244353)) % 998244353

print(solve())
