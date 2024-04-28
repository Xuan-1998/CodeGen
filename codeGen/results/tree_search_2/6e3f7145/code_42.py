def longest_palindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    max_len = 0
    result = ""

    for i in range(n):
        for j in range(i, -1, -1):
            if s[i] == s[j]:
                if i - j < 2:  # Single character or two characters are always palindromes
                    dp[i][j] = True
                elif not dp[i-1][j+1]:  # Check the substring in between
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i-1][j+1]
                if dp[i][j]:
                    if i - j + 1 > max_len:
                        max_len = i - j + 1
                        result = s[j:i+1]

    return result

# Example usage
s = input()
print(longest_palindrome(s))
