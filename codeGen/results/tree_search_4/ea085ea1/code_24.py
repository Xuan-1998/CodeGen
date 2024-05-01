from collections import defaultdict

def max_common_substrings(str1, str2):
    N = len(str1)
    M = len(str2)

    # Initialize the dp table with default values
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    # Initialize a dictionary to store memoized values
    memo = defaultdict(int)

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        result = 0
        if i > 0 and j > 0 and str1[i - 1] == str2[j - 1]:
            result += dp[i - 1][j - 1] + 1
        
        if result > 0:
            memo[(i, j)] = result
        else:
            memo[(i, j)] = max(dfs(i - 1, j), dfs(i, j - 1))

        return memo[(i, j)]

    # Calculate the maximum number of common non-overlapping substrings
    result = dfs(N, M)

    return result

# Read input strings from stdin
str1 = input().strip()
str2 = input().strip()

# Call the function to calculate the result
result = max_common_substrings(str1, str2)

# Print the result to stdout
print(result)
