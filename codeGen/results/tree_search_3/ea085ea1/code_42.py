def max_common_substrings(str1, str2):
    n = len(str1)
    memo = [[0] * (n + 1) for _ in range(n + 1)]
    prefix_hash = {}

    # Initialize base case
    for i in range(n + 1):
        memo[i][0] = memo[0][i] = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                # If the current characters match
                if str1[i - 1] not in prefix_hash or j > prefix_hash[str1[i - 1]]:
                    # Update the maximum number of common substrings
                    memo[i][j] = max(memo[i][j], memo[i - 1][j - 1] + 1)
                    prefix_hash[str1[i - 1]] = i
                else:
                    # If the current characters are overlapping, skip them
                    memo[i][j] = memo[i - 1][j - 1]
            else:
                # If the current characters don't match, skip them
                memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])

    return memo[n][n]

# Example usage
str1 = input()
str2 = input()
print(max_common_substrings(str1, str2))
