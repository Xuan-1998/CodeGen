def longest_palindrome(s):
    n = len(s)
    dp = [False] * n

    # Single characters are always palindromes
    for i in range(n):
        dp[i] = True

    max_length = 1
    start_index = 0

    # Expand around the center of each substring
    for i in range(1, n):
        for j in range(i):
            if s[j] == s[i]:
                if j + 1 <= i - 1 and dp[j + 1:i]:  # Check if the substring is palindromic
                    dp[i] = True
                    if i - j + 1 > max_length:
                        start_index = j
                        max_length = i - j + 1

    return s[start_index:start_index + max_length]
