def shortestUncommonSubsequence(S, T):
    memo = {}
    
    def dfs(i, k):
        if (i, k) in memo:
            return memo[(i, k)]
        
        if i == len(S):
            return -1
        
        if k == len(T):
            return len(S) - i
        
        last_S = S[i]
        last_T = T[k]
        
        if last_S != last_T:
            result = 1 + dfs(i + 1, k)
            memo[(i, k)] = result
            return result
        
        result = dfs(i + 1, k + 1)
        memo[(i, k)] = result
        return result
    
    return -dfs(0, 0) if (0, 0) in memo else len(S)

# test the function
S = input().strip()
T = input().strip()

print(shortestUncommonSubsequence(S, T))
