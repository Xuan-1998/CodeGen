def longest_palindromic_substring(S):
    n = len(S)
    table = [[0] * n for _ in range(n)]
    
    max_length = 0
    center_index = 0
    
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if S[i] == S[j]:
                if i == j or j - i < 3:
                    table[i][j] = True
                elif table[i + 1][j - 1]:
                    table[i][j] = True
                
                if table[i][j]:
                    if j - i + 1 > max_length:
                        max_length = j - i + 1
                        center_index = i
    
    return S[center_index: center_index + max_length]
