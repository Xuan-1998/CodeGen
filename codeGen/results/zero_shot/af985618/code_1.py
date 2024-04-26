MOD = 998244353

def main():
    n = int(input())
    A = [input().split() for _ in range(n)]

    # Initialize dp array where dp[i][j] represents the number of ways to form a subsequence
    # from the first i elements with j elements added to the multiset T.
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        if A[i - 1][0] == '+':
            x = int(A[i - 1][1])
            for j in range(i + 1):
                dp[i][j] = dp[i - 1][j]
                if j > 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % MOD
        else:
            for j in range(i):
                dp[i][j] = (dp[i - 1][j] * 2) % MOD

    # Calculate the sum of f(B) for all subsequences B
    result = 0
    for i in range(n):
        if A[i][0] == '+':
            x = int(A[i][1])
            # Calculate the expected contribution of x
            contribution = 0
            for j in range(i + 1):
                contribution = (contribution + dp[i][j] * dp[n - i - 1][j]) % MOD
            result = (result + contribution * x) % MOD

    print(result)

if __name__ == "__main__":
    main()
