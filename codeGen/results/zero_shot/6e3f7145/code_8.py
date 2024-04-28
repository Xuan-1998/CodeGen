def longest_palindromic_substring(s):
    n = len(s)
    res = ""
    
    for i in range(n):
        for j in range(i+1, n+1):
            sub = s[i:j]
            
            if sub == sub[::-1] and len(sub) > len(res):
                res = sub
                
    return res
