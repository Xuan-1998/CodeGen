from collections import deque

def canReachEnd(arr):
    n = len(arr)
    memo = {}
    
    def dfs(i):
        if i >= n:
            return True
        
        if (i,) in memo:
            return memo[(i,)]
        
        max_reachable_index = min(n-1, i+arr[i])
        for j in range(max(0, i-arr[i]), i+1):
            if dfs(j) and j == max_reachable_index:
                return True
        
        memo[(i,)] = False
        return False
    
    return dfs(0)

# Read input from stdin
arr = [int(x) for x in input().split()]

# Print the result to stdout
print(canReachEnd(arr))
