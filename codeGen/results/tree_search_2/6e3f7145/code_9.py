def longest_palindrome(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    max_length = 0
    max_palindrome = ""
    memo = {}

    def is_palindrome(start, end):
        if (start, end) in memo:
            return memo[(start, end)]
        if start >= end:
            return True

        if s[start] != s[end]:
            memo[(start, end)] = False
            return False

        memo[(start, end)] = is_palindrome(start + 1, end - 1)
        return memo[(start, end)]

    for i in range(len(s)):
        # odd length palindrome
        max_length_odd = 0
        for j in range(i, len(s)):
            if s[i] == s[j] and is_palindrome(i, j):
                max_length_odd = j - i + 1
                break

        # even length palindrome
        max_length_even = 0
        for j in range(i + 1, len(s) + 1):
            if is_palindrome(i, j - 1):
                max_length_even = j - i
                break

        if max_length_odd > max_length:
            max_length = max_length_odd
            max_palindrome = expand_around_center(i, i + max_length_odd)
        elif max_length_even > max_length:
            max_length = max_length_even
            max_palindrome = expand_around_center(i, i + max_length_even)

    return max_palindrome

s = input()
print(longest_palindrome(s))
