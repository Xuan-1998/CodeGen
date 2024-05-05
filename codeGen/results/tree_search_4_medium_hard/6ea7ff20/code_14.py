def mergeable(p):
    memo = {}
    
    def dfs(i, a_len, b_len):
        if (i, a_len, b_len) in memo:
            return memo[(i, a_len, b_len)]
        
        if i >= len(p):
            return 'YES' if a_len == 0 or b_len == 0 else 'NO'
        
        if p[i] < p[a_len-1]:
            return dfs(i+1, a_len, b_len)
        elif p[i] > p[b_len-1]:
            return dfs(i+1, a_len, b_len)
        else:
            if p[i] == p[a_len-1]:
                return 'NO'  # mismatch
            else:  # p[i] == p[b_len-1]
                return dfs(i+1, a_len-1, b_len-1)  # remove elements from both arrays
    
    result = dfs(0, n, n)
    print(result)

