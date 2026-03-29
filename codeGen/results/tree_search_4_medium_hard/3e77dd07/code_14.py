def is_scrambled(s1, s2):
    n = len(s1)
    
    # Initialize the DP table with all values set to None
    dp = [[None for _ in range(n+1)] for _ in range(n+1)]
    
    def dfs(i, j):
        if i == 0 and j == 0:
            return s1[0] == s2[0]
        
        if dp[i][j] is not None:
            return dp[i][j]
        
        if sorted(s1[:i]) != sorted(s2[:j]):
            return False
        
        for k in range(i):
            if dfs(k, j) and dfs(i-k-1, j):
                return True
        
        return False
    
    return dfs(n, n)

# Read input strings from standard input
s1 = input()
s2 = input()

print(is_scrambled(s1, s2))
