def count_matrices():
    T = int(input())  # number of test cases
    dp = [0] * (N + 1)  # dynamic programming table

    dp[1] = 1  # base case: one possible matrix with trace 1

    for i in range(2, N + 1):
        for j in range(i):
            if j < i - 1 and dp[j] * (i - 1) > 0:
                dp[i] += dp[j] * (dp[i - j - 1] if i - j - 1 >= 3 else 1)
            elif j == 1:
                dp[i] += 1

    print(dp[N])  # output the result for the given N
