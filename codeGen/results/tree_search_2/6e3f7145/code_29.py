def longest_palindromic_substring(s):
    n = len(s)
    # Initialize a 1D array to store the maximum length of palindrome ending at each position
    dp = [False] * n
    max_length = 0
    center_index = 0

    for i in range(n):
        dp[i] = True  # Initialize all one-character substrings as palindromic

    for i in range(1, n):
        for j in range(i):  # Start from the second character (since we already handled single characters)
            if s[j] == s[i]:  # Check if the characters match
                if i - j < dp[j]:
                    dp[i] = True
                    max_length = i - j + 1  # Update the maximum length of palindrome ending at this position

    return s[center_index:center_index + max_length]
