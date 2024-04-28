def longest_palindrome(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j]:
                dp[i][j] = 2 + (dp[i+1][j-1] if i+1 < j-1 else 0)
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return str(s[dp.index(max(map(max, dp)))])

# Read input from standard input
s = input()

print(longest_palindrome(s))
