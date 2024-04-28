def longest_palindrome(s):
    n = len(s)
    dp = [0] * n  # Initialize memoization array

    for i in range(1, n):
        if s[i-1] == s[i]:  # If current char is the same as previous one
            dp[i] = dp[i-1] + 2  # Extend previous palindromic substring
        else:
            dp[i] = max(dp[i-1], 0)  # Take maximum of previous palindrome or 0

    return s[max(range(n)):max(range(n))[::-1]+1]  # Return longest palindromic substring

# Example usage:
s = input()  # Read input string from stdin
print(longest_palindrome(s))  # Print the longest palindromic substring to stdout
