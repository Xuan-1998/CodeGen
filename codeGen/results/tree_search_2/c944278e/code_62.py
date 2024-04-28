def max_skill_levels(n, s):
    memo = {}
    
    def dp(i):
        if i in memo:
            return memo[i]
        
        if i == 0:
            return [0]
        
        skill_level = 1 << (n - 1) + dp(i-1)[s[i-1]] * (i % 2)
        
        memo[i] = [skill_level]
        return memo[i]
    
    return sorted([x[0] for x in dp(n)])
