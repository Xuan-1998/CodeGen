from collections import defaultdict

def min_total_cost():
    n = int(input())
    c = list(map(int, input().split()))
    s = [input() for _ in range(n)]
    
    memo = defaultdict(lambda: defaultdict(lambda: float('inf')))
    
    def dp(i, j):
        if i == 0:
            return c[j]
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        res = -1
        for k in range(j):
            if s[k] <= s[j]:
                res = min(res, dp(i-1, k) + c[j])
                break
        
        memo[(i, j)] = res
        return res
    
    return dp(n-1, n-1)

print(min_total_cost())
