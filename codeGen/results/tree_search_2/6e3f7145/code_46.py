def longest_palindromic_substring(S):
    n = len(S)
    dp = [[False] * n for _ in range(n)]

    # Initialize the diagonal elements to True (single-character palindromes)
    for i in range(n):
        dp[i][i] = True

    max_length = 0
    longest_palindrome = ""

    # Fill the dynamic programming table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if S[i] == S[j]:  # Check if characters at indices i and j are equal
                dp[i][j] = dp[i+1][j-1]  # Recursively check the substring without these two characters
            else:
                dp[i][j] = False

            # Update the longest palindromic substring found so far
            if dp[i][j]:
                if length > max_length:
                    max_length = length
                    longest_palindrome = S[i:j+1]

    return longest_palindrome
