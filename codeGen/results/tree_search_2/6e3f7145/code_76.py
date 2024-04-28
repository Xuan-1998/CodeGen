def is_palindrome(s):
    return s == s[::-1]

def longest_palindromic_substring(S):
    n = len(S)
    dp = [[0] * n for _ in range(n)]
    max_length = 0
    result = ""

    for i in range(n):
        for j in range(i, n):
            if S[i] == S[j]:
                if j - i < 3:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and j - i + 1 > max_length:
                    max_length = j - i + 1
                    result = S[i:j+1]

    return result

S = input()
print(longest_palindromic_substring(S))
