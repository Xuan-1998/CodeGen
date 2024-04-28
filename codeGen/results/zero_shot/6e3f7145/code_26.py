def longest_palindromic_substring(s):
    n = len(s)
    max_length = 0
    result = ""
    
    for i in range(n):
        # odd length palindromes
        for j in range(i+1, n+1):
            if s[i:j] == s[i:j][::-1]:
                if j - i > max_length:
                    max_length = j - i
                    result = s[i:j]
                    
        # even length palindromes
        for j in range(i+2, n+1):
            if s[i:j] == s[i:j][::-1]:
                if j - i > max_length:
                    max_length = j - i
                    result = s[i:j]
                    
    print(result)
