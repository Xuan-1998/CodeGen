def longest_palindrome(s):
    def is_palindrome(substring):
        return substring == substring[::-1]

    memo = {}

    max_length = 0
    max_palindrome = ""

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if (i, j) not in memo:
                substring = s[i:j]
                memo[(i, j)] = is_palindrome(substring)
            if memo[(i, j)] and j - i > max_length:
                max_length = j - i
                max_palindrome = substring

    return max_palindrome

# Example usage:
s = input()
print(longest_palindrome(s))
