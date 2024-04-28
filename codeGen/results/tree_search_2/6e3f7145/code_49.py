def longest_palindrome_substring(S):
    n = len(S)
    dp = [[0] * n for _ in range(n)]

    # Base case: Single characters are always palindromes
    for i in range(n):
        dp[i][i] = 1

    max_len = 0
    start_idx = 0

    # Fill up the dynamic programming table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            # Check if S[i...j] is a palindrome
            dp[i][j] = (S[i] == S[j]) and (dp[i+1][j-1])

            # Update the maximum palindromic substring found so far
            if dp[i][j] and length > max_len:
                max_len = length
                start_idx = i

    return S[start_idx:start_idx + max_len]
