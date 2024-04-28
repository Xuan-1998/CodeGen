def longest_palindromic_substring(s):
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            substr = s[i:j]
            if substr == substr[::-1]:
                return substr
