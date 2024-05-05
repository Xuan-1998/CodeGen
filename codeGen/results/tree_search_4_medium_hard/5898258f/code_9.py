def max_xor_sum(X, A):
    N = len(A)
    memo = {0: 0}
    
    def dp(i):
        if i in memo:
            return memo[i]
        
        res = 0
        for j in range(1, i+1):
            res = max(res, A[j-1] ^ (dp(j-1) - X))
        
        memo[i] = res
        return res
    
    return dp(N)

T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    print(max_xor_sum(X, A))
