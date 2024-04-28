def longest_palindromic_substring(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True  # single characters are palindromes

    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = False

    max_length = 0
    max_palindrome = ""
    for i in range(n):
        for j in range(i, n):
            if dp[i][j]:
                if len(s[i:j+1]) > max_length:
                    max_length = len(s[i:j+1])
                    max_palindrome = s[i:j+1]

    return max_palindrome

if __name__ == "__main__":
    import sys
    s = sys.stdin.read().strip()
    print(longest_palindromic_substring(s))
