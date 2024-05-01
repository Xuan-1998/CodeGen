def min_squares(n, m):
    # Define a memoization dictionary to store intermediate results
    memo = {}

    def dfs(i, j):
        if (i, j) not in memo:
            if i == 0 and j == 0:  # Base case: 0x0 rectangle
                return 0

            min_squares = float('inf')
            for k in range(1, min(i, j) + 1):
                if (i - k) * (j - k) > 0:
                    min_squares = min(min_squares, dfs(i - k, j) + dfs(k, m))

            memo[(i, j)] = min_squares
        return memo[(i, j)]

    # Calculate the minimum number of squares required to tile the rectangle
    return dfs(n, m)

# Read input from stdin and print output to stdout
n, m = map(int, input().split())
print(min_squares(n, m))
