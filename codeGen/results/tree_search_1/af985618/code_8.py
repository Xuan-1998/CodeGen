MOD = 998244353

def main():
    n = int(input())
    operations = [input().split() for _ in range(n)]

    # Initialize dp array where dp[i][j] will store the number of ways to form a subsequence
    # with j elements, considering the first i operations.
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1  # There is one way to form an empty subsequence

    for i in range(1, n + 1):
        if operations[i - 1][0] == '+':
            x = int(operations[i - 1][1])
            # Update dp for subsequences that include the current '+x' operation.
            for j in range(i, 0, -1):
                dp[i][j] = (dp[i - 1][j - 1] * x + dp[i - 1][j]) % MOD
            # Update dp for the empty subsequence.
            dp[i][0] = dp[i - 1][0]
        else:
            # Update dp for subsequences that do not include the current '-' operation.
            for j in range(i + 1):
                dp[i][j] = dp[i - 1][j]
                if j > 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % MOD

    # Calculate the answer as the sum of all dp[n][j] values.
    answer = sum(dp[n]) % MOD
    print(answer)

if __name__ == "__main__":
    main()
