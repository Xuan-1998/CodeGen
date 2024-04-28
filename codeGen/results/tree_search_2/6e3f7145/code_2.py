def longest_palindromic_substring(S):
    n = len(S)
    dp = [[0] * n for _ in range(n)]

    # Initialize the diagonal (single-character palindromes)
    for i in range(n):
        dp[i][i] = 1

    # Fill the table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if S[i] == S[j]:
                if length == 2:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i + 1][j - 1]
                if S[i] == S[j] and length > 2:
                    dp[i][j] += 2

    # Find the longest palindromic substring
    max_length = 0
    for i in range(n):
        for j in range(i, n):
            if dp[i][j] > max_length:
                max_length = dp[i][j]
                start_index = i
                end_index = j

    return S[start_index:end_index + 1]

S = input()
print(longest_palindromic_substring(S))
