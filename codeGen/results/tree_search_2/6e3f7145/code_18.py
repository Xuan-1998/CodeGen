def longest_palindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    max_len = 0
    result = ""

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                if i + 1 >= j - 1 or dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        result = s[i:j+1]

    return result

# Test the function
s = input()
print(longest_palindrome(s))
