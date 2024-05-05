import sys

def solve():
    n = int(sys.stdin.readline())
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        dp[i] = dp[i-1] * (2 - sum(dp[j] for j in range(i)))
    prob = dp[n] * pow(2, n, 998244353) % 998244353
    print(prob)

if __name__ == "__main__":
    solve()
