def longest_palindromic_substring(s):
    n = len(s)
    max_length = 0
    result = ""
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            if substring == substring[::-1] and len(substring) > max_length:
                max_length = len(substring)
                result = substring
                
    return result
