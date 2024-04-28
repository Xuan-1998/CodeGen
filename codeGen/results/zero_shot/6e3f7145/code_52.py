def longest_palindromic_substring(s):
    n = len(s)
    max_len = 0
    max_str = ""
    
    for i in range(n):
        for j in range(i, n):
            substr = s[i:j+1]
            if substr == substr[::-1] and len(substr) > max_len:
                max_len = len(substr)
                max_str = substr
                
    print(max_str)
