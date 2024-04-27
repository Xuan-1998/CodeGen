def get_orthus_hydra(heads, tails):
    # Initialize a 2D array to store the results of subproblems
    dp = [[0] * (tails + 1) for _ in range(heads + 1)]

    # Fill the dp table using dynamic programming
    for i in range(1, heads + 1):
        for j in range(1, tails + 1):
            if i == 1:
                dp[i][j] = j
            elif j == 1:
                dp[i][j] = i
            else:
                min_attempts = float('inf')
                for k in range(j):
                    attempts = 1 + max(dp[i - 1][k], dp[i][j - 1 - k])
                    if attempts < min_attempts:
                        min_attempts = attempts
                dp[i][j] = min_attempts

    # Convert the dynamic programming results into the desired output
    orthus, hydra = heads, tails
    while True:
        if dp[orthus][hydra] % 2 == 0:
            hydra -= dp[orthus][hydra] // 2
        else:
            orthus -= dp[orthus][hydra] - (dp[orthus - 1][hydra] + dp[orthus][hydra - 1])
        if orthus <= 0 or hydra <= 0:
            break

    return [orthus, hydra]

# Read input from stdin
heads, tails = map(int, input().split())

# Call the function to get the result
result = get_orthus_hydra(heads, tails)

# Print the result to stdout
print(result)
