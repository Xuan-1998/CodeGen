def is_possible(A):
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    
    memo = {}
    
    def dfs(i, k):
        if (i, k) in memo:
            return memo[(i, k)]
        
        if i < 0 or k <= 0:
            return False
        
        if k == 1:
            return True
        
        for j in range(i-1, -1, -1):
            if abs(A[i]-A[j]) > M:
                break
            if (j, k-1) not in memo:
                memo[(j, k-1)] = dfs(j, k-1)
            if memo[(j, k-1)]:
                return True
        
        memo[(i, k)] = False
        return False
    
    return dfs(N-1, K)

print(is_possible(input().split()))
