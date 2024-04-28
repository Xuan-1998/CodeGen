def longest_palindromic_substring(s):
    n = len(s)
    max_length = 0
    max_palindrome = ""
    
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if substring == substring[::-1] and len(substring) > max_length:
                max_length = len(substring)
                max_palindrome = substring
                
    return max_palindrome

s = input()
print(longest_palindromic_substring(s))
