def longest_palindrome(s):
    n = len(s)
    max_len = 0
    res = ""
    
    for i in range(n):
        for j in range(i+1, n+1):
            substr = s[i:j]
            if substr == substr[::-1]:
                if len(substr) > max_len:
                    max_len = len(substr)
                    res = substr
    
    return res

s = input()
print(longest_palindrome(s))
