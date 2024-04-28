def longest_palindromic_substring(s):
    if len(s) == 0:
        return ""

    max_length = 1
    result = s[0]

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and len(substring) > max_length:
                max_length = len(substring)
                result = substring

    return result
