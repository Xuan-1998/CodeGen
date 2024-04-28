def count_subarrays(N, K, Arr):
    memo = {}
    
    def memoized_function(i, prev_max):
        if (i, prev_max) in memo:
            return memo[(i, prev_max)]
        
        count = 0
        max_val = prev_max
        for j in range(i, N):
            max_val = max(max_val, Arr[j])
            if max_val > K:
                count += 1
            else:
                break
        
        memo[(i, prev_max)] = count
        return count
    
    total_count = 0
    for i in range(N):
        total_count += memoized_function(i, float('-inf'))
    
    return total_count

N, K = map(int, input().split())
Arr = list(map(int, input().split()))
print(count_subarrays(N, K, Arr))
