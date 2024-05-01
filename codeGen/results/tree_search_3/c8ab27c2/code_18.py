def find_shortest_uncommon_subsequence(S, T):
    # Initialize memoization dictionary
    memo = {}

    def lcs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        # Base case: If we've reached the end of either string, return 0
        if i == len(S) or j == len(T):
            return 0

        # Recursive case: Check if the current characters match
        if S[i] == T[j]:
            # If they match, recursively call lcs with incremented indices
            return 1 + lcs(i + 1, j + 1)
        else:
            # If they don't match, consider the maximum LCS without the current character
            return max(lcs(i, j + 1), lcs(i + 1, j))

    # Find the maximum length of uncommon subsequences between prefixes
    max_length = 0
    for i in range(len(S)):
        for j in range(min(i + 1, len(T))):
            max_length = max(max_length, lcs(i, j) - lcs(0, j))

    return max_length if max_length > 0 else -1

# Read input from stdin
S = input().strip()
T = input().strip()

# Call the function and print the result to stdout
print(find_shortest_uncommon_subsequence(S, T))
