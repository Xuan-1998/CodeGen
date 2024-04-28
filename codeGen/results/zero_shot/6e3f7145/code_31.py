def longest_palindrome(s):
    n = len(s)
    max_len = 0
    result = ""
    
    for i in range(n):
        for j in range(i, n):
            substr = s[i:j+1]
            if substr == substr[::-1] and len(substr) > max_len:
                max_len = len(substr)
                result = substr
                
    return result

s = input()
print(longest_palindrome(s))
