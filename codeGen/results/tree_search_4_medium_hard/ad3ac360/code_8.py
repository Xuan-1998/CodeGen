def min_cuts(s):
    n = len(s)
    dp = [[False] * (n+1) for _ in range(n+1)]

    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j-i < 2 or dp[i+1][j-1]):
                dp[i][j] = True

    cuts = 0
    last_palindrome_end = 0
    for i in range(n):
        while not dp[last_palindrome_end+1][i]:
            if s[last_palindrome_end:i].count(s[last_palindrome_end:i][0]) == len(s[last_palindrome_end:i]):
                cuts += 1
                last_palindrome_end = i
            i -= 1

    return cuts

s = input()
print(min_cuts(s))
