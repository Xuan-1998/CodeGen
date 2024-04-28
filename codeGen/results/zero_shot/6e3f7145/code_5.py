def longest_palindromic_substring():
    s = input()
    n = len(s)
    max_length = 0
    result = ""
    
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            
            if substring == substring[::-1] and len(substring) > max_length:
                max_length = len(substring)
                result = substring
                
    print(result)
