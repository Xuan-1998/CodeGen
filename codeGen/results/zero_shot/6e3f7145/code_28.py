def longest_palindromic_substring(s):
    n = len(s)
    max_len = 0
    res = ""

    for i in range(n):
        # odd length palindrome
        left, right = i, i
        while left >= 0 and right < n and s[left] == s[right]:
            if right - left + 1 > max_len:
                max_len = right - left + 1
                res = s[left:right+1]
            left -= 1
            right += 1

        # even length palindrome
        left, right = i, i + 1
        while left >= 0 and right < n and s[left] == s[right]:
            if right - left + 1 > max_len:
                max_len = right - left + 1
                res = s[left:right+1]
            left -= 1
            right += 1

    return res
