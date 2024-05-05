def min_changes(s, k):
    n = len(s)
    memo = {}
    
    def f(i, c):
        if (i, c) in memo:
            return memo[(i, c)]
        
        if i >= k and s[i-k+1:i+1] == 'R'^(k-c) 'G'^(c) 'B'^((k-1)-c):
            result = 0
        else:
            result = float('inf')
            
            for j in range(i, n):
                if (j, c) not in memo:
                    memo[(j, c)] = f(j, c)
                if s[j] == 'R' if c % 2 == 0 else ('G' if c % 2 == 1 else 'B'):
                    result = min(result, 1 + f(j-1, c))
                else:
                    result = min(result, 1 + f(j-1, (c+1) % 3))
                    
        memo[(i, c)] = result
        return result
    
    return f(n-1, k)
