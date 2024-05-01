def subset_sum_divisible(n, S, m):
    memo = {}
    
    def dfs(i, s):
        if (i, s) in memo:
            return memo[(i, s)]
        
        if i == 0:
            return s % m == 0
        
        result = False
        for j in range(len(S)):
            if S[j] <= s and S[j] + dfs(i - 1, s - S[j]) % m == 0:
                result = True
                break
        
        memo[(i, s)] = result
        return result
    
    return dfs(n, sum(S))

# Input
n = int(input())
m = int(input())
S = list(map(int, input().split()))

print(subset_sum_divisible(n, S, m))
