def longest_palindrome():
    s = input()
    n = len(s)
    max_length = 0
    max_palindrome = ""
    
    for i in range(n):
        for j in range(i+1, n+1):
            substr = s[i:j]
            if substr == substr[::-1] and len(substr) > max_length:
                max_length = len(substr)
                max_palindrome = substr
                
    print(max_palindrome)

longest_palindrome()
