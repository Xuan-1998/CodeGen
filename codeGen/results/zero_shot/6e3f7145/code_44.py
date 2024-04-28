def longest_palindromic_substring(s):
    n = len(s)
    max_length = 0
    max_palindrome = ""
    
    for i in range(n):
        # odd length palindrome
        for j in range(i+1, n+1):
            if s[i:j] == s[i:j][::-1]:
                if len(s[i:j]) > max_length:
                    max_length = len(s[i:j])
                    max_palindrome = s[i:j]
                    
        # even length palindrome
        for j in range(i+2, n+1):
            if s[i+1:j] == s[i+1:j][::-1]:
                if len(s[i+1:j]) > max_length:
                    max_length = len(s[i+1:j])
                    max_palindrome = s[i+1:j]
                    
    print(max_palindrome)
