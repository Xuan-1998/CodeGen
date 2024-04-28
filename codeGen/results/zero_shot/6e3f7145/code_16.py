def longest_palindromic_substring(s):
    n = len(s)
    longest_palindrome = ""
    
    for i in range(n):
        for j in range(i+1, n+1):
            substring = s[i:j]
            
            if substring == substring[::-1] and len(substring) > len(longest_palindrome):
                longest_palindrome = substring
                
    return longest_palindrome

s = input()
print(longest_palindromic_substring(s))
