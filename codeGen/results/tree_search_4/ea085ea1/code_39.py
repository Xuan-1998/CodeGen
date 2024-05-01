def common_substrings(str1, str2):
    n = len(str1)
    m = len(str2)

    # Initialize 3D DP table with zeros
    dp = [[[0] * (min(n+1, m+1)) for _ in range(min(n+1, m+1))] for _ in range(4)]

    # Base case: If the strings are empty, return 0
    if n == 0 and m == 0:
        return 0

    # Initialize memoization dictionary
    memo = {}

    def dfs(i, j, k):
        key = (i, j, k)
        if key in memo:
            return memo[key]

        # If the current substring is out of bounds or doesn't match
        if i > n or j > m or str1[i-k] != str2[j-k]:
            result = 0
        else:
            # Consider all possible lengths of substrings ending at positions i and j
            for length in range(1, min(i+1, j+1)+1):
                if k < length:
                    break

                # Check if there are common non-overlapping substrings that end at positions i and j with the same substring length k
                if dp[0][i-length][k] and dp[0][j-length][k]:
                    result = max(result, 1 + dfs(i-length, j-length, k-1))
                else:
                    result = max(result, dfs(i-length, j-length, k))

        # Store the intermediate result in memoization dictionary
        memo[key] = result

        return result

    return dfs(0, 0, n)  # Return dp[0][n][n], which represents the maximum number of common non-overlapping substrings between str1 and str2

# Read input from standard input
str1 = input().strip()
str2 = input().strip()

# Print the output to standard output
print(common_substrings(str1, str2))
