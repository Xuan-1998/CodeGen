===BEGIN CODE===
def calculate_probability(n, m, h, s):
    memo = {}
    
    def dp(d, n):
        if (d, n) in memo:
            return memo[(d, n)]
        
        if d == h:
            result = 1 if n >= n else -1
        elif d < h and n < s[h-1]:
            result = dp(h, s[h-1])
        else:
            total_players = sum(s[:h])
            result = (dp(h, s[h-1]) * (n + 1) + dp(d, n)) / (2**m)
        
        memo[(d, n)] = result
        return result
    
    if m < h or sum(s) < n:
        return -1.0
    else:
        return dp(0, 0)
