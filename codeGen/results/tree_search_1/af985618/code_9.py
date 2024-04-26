MOD = 998244353

def main():
    n = int(input().strip())
    A = [input().strip() for _ in range(n)]

    # Initialize the dp array where dp[i][j] will store the sum of all subsequences
    # that end at position i with the last added value j.
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    # This array will help us to calculate the contribution of each element when it is the smallest in the multiset.
    smallest = [0] * (n + 1)

    for i in range(1, n + 1):
        if A[i - 1][0] == '+':
            x = int(A[i - 1][1:])
            for j in range(i + 1):
                dp[i][j] = dp[i - 1][j]  # We can choose not to include A[i-1] in our subsequence.
                if j > 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] + smallest[j - 1]) % MOD  # Include A[i-1] in the subsequence.
            smallest[0] = (smallest[0] + x) % MOD  # Update the contribution for being the smallest.
            for j in range(1, i + 1):
                smallest[j] = (smallest[j] + dp[i - 1][j - 1]) % MOD
        else:
            for j in range(i + 1):
                dp[i][j] = (dp[i - 1][j] * 2) % MOD  # Each subsequence can either include or exclude the '-' operation.
            for j in range(i + 1):
                smallest[j] = (smallest[j] * 2) % MOD

    # Sum up the values of dp[n][j] for all j to get the result.
    result = sum(dp[n]) % MOD
    print(result)

if __name__ == "__main__":
    main()
