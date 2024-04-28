from collections import defaultdict

def partition_array():
    t = int(input())
    dp = defaultdict(int)
    
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        max_partition = 0
        total_sum = sum(arr)
        left_sum = 0
        
        for i in range(n+1):
            if i > 0:
                left_sum += arr[i-1]
                
                if left_sum == (total_sum - left_sum):
                    max_partition += 1
                    left_sum = 0
            
            dp[i] = max(0 if i == 0 else dp[i-1], i // 2 if i % 2 == 0 and sum(arr[:i//2+1]) == sum(arr[i//2+1:]))
        
        print(max_partition)

partition_array()
