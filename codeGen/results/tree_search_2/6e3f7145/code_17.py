def longest_palindromic_substring(s):
    memo = {}

    def helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == j:
            return s[i]

        if s[i] != s[j]:
            return ""

        length = j - i + 1

        if length <= 3:
            return s[i:j+1]

        for k in range(i, j):
            prefix = helper(i, k)
            suffix = helper(k+1, j)

            if len(prefix) == len(suffix) and prefix + suffix == (prefix + suffix)[::-1]:
                return prefix + suffix

        memo[(i, j)] = s[i:j+1]
        return s[i:j+1]

    max_length = 0
    longest_substring = ""

    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = helper(i, j)
            if len(substr) > max_length:
                max_length = len(substr)
                longest_substring = substr

    return longest_substring
