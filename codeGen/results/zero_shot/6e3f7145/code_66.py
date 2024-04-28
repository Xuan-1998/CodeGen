def longest_palindromic_substring():
    s = input()
    n = len(s)
    max_length = 0
    result = ""
    
    for i in range(n):
        for j in range(i, n):
            substr = s[i:j+1]
            if substr == substr[::-1]:
                if len(substr) > max_length:
                    max_length = len(substr)
                    result = substr
                    
    print(result)
