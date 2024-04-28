def longest_palindrome(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    max_length = 0
    result = ""

    for i in range(len(s)):
        # odd length palindrome
        if i > 0 and i < len(s) - 1:
            result = max(result, expand_around_center(i, i), key=len)
        # even length palindrome
        if i < len(s) - 1:
            result = max(result, expand_around_center(i, i + 1), key=len)

    print(result)
