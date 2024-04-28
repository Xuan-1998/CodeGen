def longest_palindrome(s):
    n = len(s)
    longest = ""
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substr = s[i:j]
            if substr == substr[::-1] and len(substr) > len(longest):
                longest = substr
                
    for i in range(n):
        substr = s[i]
        while i + len(substr) <= n:
            if substr != substr[::-1]:
                break
            if len(substr) > len(longest):
                longest = substr
            substr += s[i + len(substr)]
    print(longest)
