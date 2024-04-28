def longest_palindromic_substring(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Initialize the diagonal cells to 1, since a single character is always a palindrome.
    for i in range(n):
        dp[i][i] = 1

    max_length = 0
    max_palindrome = ""

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                # If the characters at the midpoint are equal, we can extend the palindrome.
                if length == 2 or dp[i+1][j-1]:
                    dp[i][j] = 1
                    if length > max_length:
                        max_length = length
                        max_palindrome = s[i:j+1]
            else:
                # If the characters at the midpoint are not equal, we cannot extend the palindrome.
                dp[i][j] = 0

    return max_palindrome

# Read the input string from standard input.
s = input()

# Call the function to find the longest palindromic substring.
print(longest_palindromic_substring(s))
