def longest_palindrome(s):
    n = len(s)
    dp = {}

    def expand_around_center(start, end):
        if (start, end) in dp:
            return dp[(start, end)]

        if start == end:
            return s[start]

        if s[start] != s[end]:
            return ""

        length = end - start
        if length % 2 == 1:
            middle = s[start + length // 2]
            for i in range(length // 2):
                if s[start + i] != middle or s[end - i] != middle:
                    return s[start:(end - i) + 1]

        dp[(start, end)] = s[start:end+1]
        return s[start:end+1]

    max_length = 0
    longest_palindrome = ""

    for i in range(n):
        for j in range(i + 1, n + 1):
            palin = expand_around_center(i, j - 1)
            if len(palin) > max_length:
                max_length = len(palin)
                longest_palindrome = palin

    return longest_palindrome
