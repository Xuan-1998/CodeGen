def longest_palindromic_substring(S):
    n = len(S)
    dp = [False] * n

    for i in range(n):
        if S[i] == S[i]:  # single-character palindrome
            dp[i] = True

    for i in range(n):
        for k in range(1, (n - i) // 2 + 1):  # extend outward from the middle
            if S[i:i+k] == S[i+k-1:i:-1]:  # check if substring is a palindrome
                dp[i + k] = True

    max_len = 0
    max_palindrome = ""

    for i in range(n):
        if dp[i]:
            j = i - 1
            while j >= 0 and dp[j]:
                j -= 1
            palindromic_substring = S[j + 1:i+1]
            if len(palindromic_substring) > max_len:
                max_len = len(palindromic_substring)
                max_palindrome = palindromic_substring

    return max_palindrome
