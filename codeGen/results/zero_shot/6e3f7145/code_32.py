def longest_palindrome(s):
    n = len(s)
    max_length = 0
    max_palindrome = ""
    
    for i in range(n):
        for j in range(i, n):
            if s[i:j+1] == s[i:j+1][::-1]:
                if len(s[i:j+1]) > max_length:
                    max_length = len(s[i:j+1])
                    max_palindrome = s[i:j+1]
                    
    print(max_palindrome)
