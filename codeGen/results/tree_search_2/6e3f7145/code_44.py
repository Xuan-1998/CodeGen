def longest_palindromic_substring(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    max_length = 0
    start = 0

    for i in range(n):
        for j in range(i, n):
            if s[i] == s[j]:
                if j - i < 2:  # Single character or two characters (i.e., a palindrome)
                    dp[i][j] = True
                elif j - i == 2:
                    if s[i] == s[j-1]:  # Check for "aba" case
                        dp[i][j] = True
                    else:
                        continue
                else:
                    dp[i][j] = dp[i+1][j-1]

                if dp[i][j] and j - i + 1 > max_length:
                    max_length = j - i + 1
                    start = i

    return s[start:start+max_length]
