def longest_palindrome(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    max_length = 0
    max_palindrome = ""
    for i in range(len(s)):
        # Odd-length palindrome
        palindrome = expand_around_center(i, i)
        if len(palindrome) > max_length:
            max_length = len(palindrome)
            max_palindrome = palindrome

        # Even-length palindrome
        palindrome = expand_around_center(i, i + 1)
        if len(palindrome) > max_length:
            max_length = len(palindrome)
            max_palindrome = palindrome

    return max_palindrome

# Read input from standard input
s = input()

print(longest_palindrome(s))
