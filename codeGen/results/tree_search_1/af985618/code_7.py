import sys

MOD = 998244353

def main():
    n = int(sys.stdin.readline().strip())
    A = [sys.stdin.readline().strip().split() for _ in range(n)]

    # dp[i][j] will store the number of ways to form a sum j with i elements.
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    # prefix_sums will store the sum of all dp[i][j] for fixed i and all j.
    prefix_sums = [[0] * (n + 1) for _ in range(n + 1)]
    prefix_sums[0][0] = 1

    for i in range(1, n + 1):
        operation, x = A[i - 1]
        if operation == "+":
            x = int(x)
            for j in range(i + 1):
                for k in range(j * x + 1):
                    if j > 0 and k >= x:
                        dp[j][k] = (dp[j][k] + dp[j - 1][k - x]) % MOD
                    dp[j][k] = (dp[j][k] + dp[j][k]) % MOD
                prefix_sums[i][j] = (prefix_sums[i - 1][j] + dp[j][j * x]) % MOD
        else:
            for j in range(i + 1):
                for k in range(j * x + 1):
                    dp[j][k] = dp[j][k]

    result = 0
    for i in range(1, n + 1):
        result = (result + prefix_sums[n][i]) % MOD

    print(result)

if __name__ == "__main__":
    main()
