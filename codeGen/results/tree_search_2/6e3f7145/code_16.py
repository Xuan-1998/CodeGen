def is_palindrome(s):
    return s == s[::-1]

def longest_palindromic_substring(s):
    memo = {}

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i >= j:
            return ""

        if is_palindrome(s[i:j+1]):
            memo[(i, j)] = s[i:j+1]
            return s[i:j+1]

        result = ""
        for k in range(i, j):
            left = dfs(i, k)
            right = dfs(k+1, j)
            if len(left) + len(right) > len(result):
                result = left + right

        memo[(i, j)] = result
        return result

    max_length = 0
    longest_palindromic_substring = ""

    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = dfs(i, j-1)
            if len(substring) > max_length:
                max_length = len(substring)
                longest_palindromic_substring = substring

    return longest_palindromic_substring
