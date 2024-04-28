def max_count(K, arr):
    memo = {}
    
    def dfs(i, max_val):
        if (i, max_val) in memo:
            return memo[(i, max_val)]
        
        count = 0
        if max_val > K:
            for j in range(i, len(arr)):
                if arr[j] > K:
                    count += dfs(j+1, max(arr[j], max_val))
                else:
                    break
            count += 1
        
        memo[(i, max_val)] = count
        return count
    
    return dfs(0, float('inf'))

N, K = map(int, input().split())
Arr = list(map(int, input().split()))
print(max_count(K, Arr))
