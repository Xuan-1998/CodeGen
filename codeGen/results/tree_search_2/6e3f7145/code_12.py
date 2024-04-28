def longest_palindrome(s):
    memo = {}

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_length:
                max_length = right - left + 1
                result = s[left:right+1]
            left -= 1
            right += 1

    max_length = 0
    result = ""

    for i in range(len(s)):
        for j in range(i, len(s)):
            if (i == 0 or memo.get((i-1, j), False)) and s[i] == s[j]:
                expand_around_center(i, j)
                break

    return result
