def is_palindrome(s):
    n = len(s)
    memo = {}

    def helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i >= j:
            return True
        if s[i] != s[j]:
            return False
        memo[(i, j)] = helper(i+1, j-1)
        return memo[(i, j)]

    return helper(0, n-1)

def longest_palindromic_substring(s):
    max_length = 0
    result = ""
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if is_palindrome(s[i:j]):
                if j - i > max_length:
                    max_length = j - i
                    result = s[i:j]
    return result

# Read input from stdin
s = input()

# Print the output to stdout
print(longest_palindromic_substring(s))
