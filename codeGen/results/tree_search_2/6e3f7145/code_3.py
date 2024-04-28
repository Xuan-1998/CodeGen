def longest_palindromic_substring(S):
    n = len(S)
    table = [[False] * n for _ in range(n)]
    
    max_length = 0
    center_index = 0
    
    for i in range(n):
        table[i][i] = True
        
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            if S[i] == S[j]:
                table[i][j] = (length == 2 or table[i+1][j-1])
                
                if table[i][j] and length > max_length:
                    max_length = length
                    center_index = i
    return S[center_index:center_index + max_length]
