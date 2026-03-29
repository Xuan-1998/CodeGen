def min_palindrome_cuts(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    # Base case: single character is always palindromic
    for i in range(n):
        dp[i][i] = True

    # Fill up the dp table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:  # Check if characters match at both ends
                if length == 2:  # If length is 2, the substring is always palindromic
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]  # Recurse on the inner substring

    # Count the minimum number of cuts needed
    cuts = 0
    for i in range(n):
        if not dp[0][i]:  # If the substring from 0 to i is not palindromic
            cuts += 1

    return cuts

# Example usage:
s = input()
print(min_palindrome_cuts(s))
