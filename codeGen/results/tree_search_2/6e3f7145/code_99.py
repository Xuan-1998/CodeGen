def longest_palindromic_substring(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    max_length = 0
    result = ""

    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j] and (j-i < 3 or dp[i+1][j-1]):
                dp[i][j] = True
                if length > max_length:
                    max_length = length
                    result = s[i:j+1]

    return result

# Example usage:
input_string = input()
print(longest_palindromic_substring(input_string))
