def minCuts(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    # All substrings are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for palindrome of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True

    # Check for palindrome of length 3 and more
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                break

    # Calculate the number of cuts
    cuts = 0
    for i in range(n):
        if not dp[0][i]:
            cuts += 1
    return cuts

# Read the input string from standard input
s = input()

# Print the minimum number of cuts required to partition the string into palindromic substrings
print(minCuts(s))
