def longest_palindromic_substring(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    max_length = 0
    result = ""

    for i in range(n):
        dp[i][i] = True

    for cl in range(2, n+1):
        for i in range(n-cl+1):
            j = i + cl - 1
            if cl == 2:
                dp[i][j] = (s[i] == s[j])
            else:
                dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
            if dp[i][j] and cl > max_length:
                max_length = cl
                result = s[i:j+1]

    return result

s = input()
print(longest_palindromic_substring(s))
