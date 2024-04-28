def longest_palindromic_substring(s):
    n = len(s)
    table = [[0 for _ in range(n)]for _ in range(n)]
    
    max_length = 1
    start_index = 0
    
    for i in range(n):
        table[i][i] = True
        
    for cl in range(2, n+1):
        for i in range(n-cl+1):
            j = i+cl-1
            
            if s[i] == s[j]:
                if cl == 2:
                    table[i][j] = True
                else:
                    table[i][j] = table[i+1][j-1]
                
                if table[i][j] and cl > max_length:
                    start_index = i
                    max_length = cl
                    
    return s[start_index:start_index + max_length]

s = input()
print(longest_palindromic_substring(s))
