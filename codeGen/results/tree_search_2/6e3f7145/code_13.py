def longest_palindrome(s):
    n = len(s)
    dp = {i: {j: s[i:j+1] == s[i:j+1][::-1] for j in range(i, n)} for i in range(n)}

    max_length = 0
    max_palindrome = ""

    for i in range(n):
        for j in range(i, n):
            if dp[i][j]:
                if len(s[i:j+1]) > max_length:
                    max_length = len(s[i:j+1])
                    max_palindrome = s[i:j+1]

    return max_palindrome
