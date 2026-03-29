import sys

def solve():
    n = int(sys.stdin.readline())
    dp = [[0] * 2 for _ in range(n + 1)]
    dp[0][0] = 1  # base case: no towns get signal from any tower
    for i in range(1, n + 1):
        for j in range(2):
            if j == 0:
                dp[i][j] = (dp[i - 1][0] + dp[i - 1][1]) % 998244353
            else:
                dp[i][j] = dp[i - 1][0]
    count_valid_configs = dp[n][1]
    total_configs = 2 ** n
    prob = (count_valid_configs * pow(2, n, 998244353)) % 998244353
    print(prob)

if __name__ == "__main__":
    solve()
