def longest_palindromic_substring(s):
    memo = {}
    def is_palindrome(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i >= j:
            return True
        if s[i] != s[j]:
            return False
        memo[(i, j)] = s[i+1:j] is not None and is_palindrome(i+1, j-1)
        return memo[(i, j)]

    max_len = 0
    result = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_palindrome(i, j) and j-i+1 > max_len:
                max_len = j-i+1
                result = s[i:j+1]
    return result

# Test the function
s = input()
print(longest_palindromic_substring(s))
