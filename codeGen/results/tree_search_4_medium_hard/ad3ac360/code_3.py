# Read the input string
n = int(input())
s = input()

# Initialize a 2D DP table with all False values
dp = [[False] * n for _ in range(n)]

# Base case: an empty string is a palindrome
dp[0][0] = True

# Fill up the diagonal elements, since single-character strings are always palindromes
for i in range(n):
    dp[i][i] = True

# Fill up the upper triangle of the DP table
for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        if s[i] == s[j]:
            dp[i][j] = (length == 1) or dp[i + 1][j - 1]
        else:
            dp[i][j] = False

# Calculate the minimum number of cuts needed
cuts = 0
for i in range(n):
    if not dp[0][i]:
        cuts += 1
