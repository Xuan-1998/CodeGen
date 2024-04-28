def longest_palindromic_substring(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    max_length = 0
    longest_palindromic_substring = ""
    for i in range(len(s)):
        palindromic_substring1 = expand_around_center(i, i)
        if len(palindromic_substring1) > max_length:
            max_length = len(palindromic_substring1)
            longest_palindromic_substring = palindromic_substring1

        palindromic_substring2 = expand_around_center(i, i + 1)
        if len(palindromic_substring2) > max_length:
            max_length = len(palindromic_substring2)
            longest_palindromic_substring = palindromic_substring2

    return longest_palindromic_substring
