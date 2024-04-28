def longest_palindromic_substring(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    max_length = 0
    longest_palindrome = ""

    for i in range(len(s)):
        # Odd-length palindrome: consider both odd and even cases
        palindrome = expand_around_center(i, i)
        if len(palindrome) > max_length:
            max_length = len(palindrome)
            longest_palindrome = palindrome

        # Even-length palindrome: consider both even and odd cases
        palindrome = expand_around_center(i, i + 1)
        if len(palindrome) > max_length:
            max_length = len(palindrome)
            longest_palindrome = palindrome

    return longest_palindrome


# Receive input from stdin
s = input()

# Print the result to stdout
print(longest_palindromic_substring(s))
