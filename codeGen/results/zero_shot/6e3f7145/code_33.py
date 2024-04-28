def longest_palindrome(s):
    n = len(s)
    max_len = 0
    max_palindrome = ""
    
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            
            if substring == substring[::-1] and len(substring) > max_len:
                max_len = len(substring)
                max_palindrome = substring
                
    print(max_palindrome)

s = input()
longest_palindrome(s)
