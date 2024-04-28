def partition_times(arr):
    n = len(arr)
    dp = {0: 0}
    
    for i in range(1, n+1):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i:])
        
        max_partitions = 0
        
        for j in range(i-1, -1, -1):
            if left_sum == right_sum:
                max_partitions = max(max_partitions, dp.get(j-1, 0) + 1)
            
            left_sum -= arr[j]
            right_sum += arr[j]
        
        dp[i] = max_partitions
    
    return dp[n]

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    print(partition_times(arr))
