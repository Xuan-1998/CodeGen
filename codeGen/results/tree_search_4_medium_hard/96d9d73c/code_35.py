from collections import defaultdict

def partition_array(N, K, M):
    A = list(map(int, input().split()))
    
    # Initialize the memo dictionary
    memo = {(i, j, m): False for i in range(N+1) for j in range(K+1) for m in range(M+1)}
    
    def dp(i, k):
        if memo[i][k]:
            return True
        
        if i < K:
            return False
        
        max_val = max(A[:i])
        min_val = min(A[:i])
        
        for j in range(1, min(k, (i+1)//k)+1):
            if all(abs(val - A[j-1]) <= M for val in A[j:i]):
                memo[i][k] = dp(j-1, j)
                return True
        
        memo[i][k] = False
        return False
    
    # Check if it's possible to partition the entire array into K partitions with maximum difference M
    return dp(N, K)

# Read input from stdin and print output to stdout
print(partition_array(*map(int, input().split())))
