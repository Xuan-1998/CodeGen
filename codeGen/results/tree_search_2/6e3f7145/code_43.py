def longest_palindromic_substring(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Initialize base case: single characters are palindromes
    for i in range(n):
        dp[i][i] = 1

    max_length = 0
    longest_palindrome = ""

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            # If characters at indices i and j are equal, consider the substring S[i...j]
            if s[i] == s[j]:
                # If j - i + 1 is even (i.e., length is odd), check if the middle character matches
                if (j - i + 1) % 2 == 0:
                    dp[i][j] = dp[(i + 1)][(j - 1)] or s[i] == s[j]
                else:
                    # If j - i + 1 is odd, check if the middle character matches and the surrounding characters form a palindrome
                    dp[i][j] = dp[(i + 1)][(j - 1)] or (s[i] == s[j] and dp[(i + 2)][(j - 1)])

                # Update max_length and longest_palindrome if necessary
                if dp[i][j]:
                    max_length = j - i + 1
                    longest_palindrome = s[i:j+1]

    return longest_palindrome

# Example usage:
s = input()
print(longest_palindromic_substring(s))
