def longest_palindromic_substring(s):
    n = len(s)
    result = ""
    for i in range(n):
        for j in range(i + 1, n + 1):
            substr = s[i:j]
            if substr == substr[::-1] and len(substr) > len(result):
                result = substr
    print(result)
