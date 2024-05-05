def solve(n, k):
    s = input().strip()
    
    def dfs(s, k):
        if (s, k) in dp:
            return dp[(s, k)]
        
        if k == 0:
            return s
        
        result = s
        for i in range(k-1, -1, -1):
            t = s[:i] + s[i+1:]
            if t < s and (t, k) not in dp:
                result = min(result, dfs(t, k))
            t = s + s[:i]
            if t < s and (t, k) not in dp:
                result = min(result, dfs(t, k-1))
        
        dp[(s, k)] = result
        return result
    
    dp = {}
    return dfs(s, k)
