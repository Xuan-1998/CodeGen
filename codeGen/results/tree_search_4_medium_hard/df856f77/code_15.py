def min_operations():
    N = int(input())
    A = list(map(int, input().split()))
    
    # Initialize memo dictionary
    memo = {(i, j): float('inf') for i in range(N) for j in range(N)}
    memo[(0, 0)] = 0
    
    def dp(i, j):
        if (i, j) not in memo:
            res = float('inf')
            for k in range(i-1, -1, -1):
                if A[k+1] > A[k]:
                    res = min(res, dp(k, j-1) + (A[k+1]-A[k]+1))
                else:
                    res = dp(k, j)
                    break
            memo[(i, j)] = res
        return memo[(i, j)]
    
    return dp(N-1, N-2)

print(min_operations())
