def longest_palindromic_substring(s):
    memo = {}

    def is_palindrome(s, e):
        if (s, e) in memo:
            return memo[(s, e)]

        c = s + e // 2
        if e % 2 == 0:  # even length
            center_char = s + c - 1
            left_half = is_palindrome(s, center_char)
            right_half = is_palindrome(center_char, e)
            return left_half and right_half
        else:  # odd length
            return (s + c == e) or (is_palindrome(s, c) and is_palindrome(c, e))

    max_len = 0
    longest_palindrome = ""

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if is_palindrome(i, j - 1):
                if j - i > max_len:
                    max_len = j - i
                    longest_palindrome = s[i:j]

    return longest_palindrome

# Example usage:
input_string = input()
print(longest_palindromic_substring(input_string))
