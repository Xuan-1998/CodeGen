def min_perfect_squares(n):
    perfect_squares = generate_perfect_squares(n)
    dp = [[0] * (n + 1) for _ in range(len(perfect_squares) + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, len(perfect_squares) + 1):
            if perfect_squares[j - 1] > i:
                dp[j][i] = dp[j - 1][i]
            else:
                min_val = float('inf')
                for k in range(j):
                    if perfect_squares[k] <= i:
                        min_val = min(min_val, dp[k][i - perfect_squares[j - 1]] + 1)
                dp[j][i] = min_val
    
    return dp[-1][-1]

# Example usage:
n = int(input())  # Read input from stdin
result = min_perfect_squares(n)
print(result)  # Print the minimum number of perfect squares required to stdout
