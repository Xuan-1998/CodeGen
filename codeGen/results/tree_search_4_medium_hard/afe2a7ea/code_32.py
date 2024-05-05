import sys

def solve():
    n = int(sys.stdin.readline())
    MOD = 998244353
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n):
        dp[i] = (dp[i - 1] * 2) % MOD
    print(dp[n])

if __name__ == "__main__":
    solve()
