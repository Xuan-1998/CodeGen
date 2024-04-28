def min_squares(n, m):
    # Create a 2D array to store the results of subproblems
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    def calculate_min_squares(i, j):
        # Base case: when i == 1 or j == 1, there are no possible squares
        if i == 1:
            return min(j // k + 1 for k in range(1, j + 1))
        elif j == 1:
            return i
        else:
            # Calculate the minimum number of squares that tile a rectangle of size i x (i + k) when k satisfies 1 <= k <= m
            if dp[i][j] != 0:
                return dp[i][j]
            result = float('inf')
            for k in range(1, j + 1):
                # Calculate the minimum number of squares that tile a rectangle of size i x (i + k) when k satisfies 1 <= k <= m
                result = min(result, calculate_min_squares(i, k) + (j - k) // k + 1)
            dp[i][j] = result
            return result

    # Calculate the minimum number of squares that tile a rectangle of size n x m
    return calculate_min_squares(n, m)

# Read input from stdin
n, m = map(int, input().split())

# Print the output to stdout
print(min_squares(n, m))
