def isScramble(s1, s2):
    n = len(s1)
    
    def dfs(i, j):
        if i == 0:
            return s1[:j] == s2[:j]
        
        dp = [[False] * (n - i) for _ in range(n - j)]
        
        for k in range(1, n - i):
            if s1[i - 1: i + k] == s2[j - 1: j + k]:
                dp[0][k - 1] = dfs(i, j + k)
                
        for k in range(n - i):
            if s1[i - 1: i + k] == s2[j - 1: j + k]:
                for l in range(1, n - j - k):
                    dp[k][l - 1] = dfs(i + k, j + l)
                    
        return any(dp)

    return dfs(0, 0)


# Read input from standard input
s1 = input()
s2 = input()

print(isScramble(s1, s2))
