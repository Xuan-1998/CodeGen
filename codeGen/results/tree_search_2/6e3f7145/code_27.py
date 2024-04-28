def longest_palindrome(S):
    n = len(S)
    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    max_len = 0
    max_palindrome = ""

    for i in range(n - 1):
        for j in range(i + 1, n):
            if S[i] == S[j]:
                if i + 1 == j or dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        max_palindrome = S[i:j+1]

    return max_palindrome

# Example usage
S = input()
print(longest_palindrome(S))
