def longest_palindrome(s):
    n = len(s)
    max_len = 0
    result = ""
    
    for i in range(n):
        for j in range(i+1, n+1):
            sub = s[i:j]
            if sub == sub[::-1] and len(sub) > max_len:
                max_len = len(sub)
                result = sub
    
    return result

s = input()
print(longest_palindrome(s))
