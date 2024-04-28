def longest_palindrome(s):
    n = len(s)
    max_len = 0
    start = 0
    
    for i in range(n):
        for j in range(i+1, n+1):
            if s[i:j] == s[i:j][::-1]:
                if j - i > max_len:
                    max_len = j - i
                    start = i
                    
    return s[start:start+max_len]
