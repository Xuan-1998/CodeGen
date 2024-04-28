def longest_palindromic_substring(s):
    if len(s) == 0:
        return ""

    max_length = 0
    max_palindrome = ""
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if substring == substring[::-1] and len(substring) > max_length:
                max_length = len(substring)
                max_palindrome = substring
                
    return max_palindrome
