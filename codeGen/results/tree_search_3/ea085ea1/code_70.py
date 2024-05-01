def max_common_substrings(str1, str2):
    N = len(str1)
    M = len(str2)

    # Initialize the dp array with zeros
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    memo = {}

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        max_substrings = 0
        
        while i < N and j < M:
            if str1[i] == str2[j]:
                max_substrings += 1
                i += 1
                j += 1
            else:
                break
        
        dp[i][j] = max_substrings
        memo[(i, j)] = max_substrings
        
        return max_substrings

    # Fill up the dp array using a nested loop
    for i in range(N + 1):
        for j in range(M + 1):
            if i == N or j == M:
                dp[i][j] = 0
            else:
                dp[i][j] = dfs(i, j)

    # Return the value stored at the last position in the dp array as the maximum number of common non-overlapping substrings
    return dp[N][M]

# Example usage:
str1 = input()
str2 = input()

print(max_common_substrings(str1, str2))
