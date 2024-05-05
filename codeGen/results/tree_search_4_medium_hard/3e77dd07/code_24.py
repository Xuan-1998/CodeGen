class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        memo = {}
        
        def dfs(i, j, length):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if length == 0:
                return True
            
            for k in range(1, length + 1):
                if sorted(s1[i:i+k]) != sorted(s2[j:j+k]):
                    continue
                if dfs(i, j, k) and dfs(i+k, j+k, length-k):
                    memo[(i, j)] = True
                    return True
            
            memo[(i, j)] = False
            return False
        
        return dfs(0, 0, len(s1))
