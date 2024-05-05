def count_matrices():
    T = int(input())  # Read input from stdin
    dp = [0] * (N + 1)  # Initialize DP table with zeros

    for i in range(3, N + 1):  # Start from trace 3 (since it's a 2x2 matrix)
        if i % 2 == 0:  # Even trace
            dp[i] = sum(dp[j] * (i - j) // 2 for j in range(i))
        else:  # Odd trace
            dp[i] = sum(dp[j] * (i - j + 1) // 2 for j in range(i))

    return [dp[n] for _ in range(T)]  # Read T test cases and output results

print(*count_matrices(), sep='\n')  # Print the results to stdout
