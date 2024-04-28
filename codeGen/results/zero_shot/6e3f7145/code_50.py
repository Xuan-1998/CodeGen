def longest_palindromic_substring(s):
    n = len(s)
    max_length = 0
    max_palindrome = ""
    
    for i in range(n):
        for j in range(i+1, n+1):
            substring = s[i:j]
            
            if substring == substring[::-1]:
                if len(substring) > max_length:
                    max_length = len(substring)
                    max_palindrome = substring
    
    print(max_palindrome)

longest_palindromic_substring(input())
