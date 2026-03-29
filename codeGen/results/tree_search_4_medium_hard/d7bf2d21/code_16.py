from collections import defaultdict

def longest_increasing_subsequences(arr):
    n = len(arr)
    memo = [[-1]*n for _ in range(n)]
    
    def dp(i, j):
        if j == 0:
            return 1
        if memo[i][j] != -1:
            return memo[i][j]
        
        ans = 1
        for k in range(j):
            if arr[k] < arr[i]:
                ans = max(ans, dp(k, k) + 1)
        
        memo[i][j] = ans
        return ans
    
    max_len = 0
    for i in range(n):
        for j in range(i+1):
            max_len = max(max_len, dp(i, j))
    
    return max_len

arr = list(map(int, input().split()))
print(longest_increasing_subsequences(arr))
