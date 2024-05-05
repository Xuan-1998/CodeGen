def solve():
    t = int(input())  # Read number of test cases

    for _ in range(t):
        n, m = map(int, input().split())  # Read initial number and operations

        dp = [[0] * (m + 1) for _ in range(11)]  # Initialize DP table
        for i in range(10):  # Preprocess dp[0][j]
            dp[i][0] = 1

        for j in range(m + 1):
            for n_digits in range(1, 11):
                if n_digits == 1:  # Single-digit number
                    dp[n_digits][j] = 1
                else:
                    max_digits = ceil(log10(n_digits)) if n_digits > 0 else 0
                    dp[n_digits][j] = 1 + min(dp[n_digits - 1][j - 1], max_digits)

        print(dp[1][m])  # Print the final result

solve()
