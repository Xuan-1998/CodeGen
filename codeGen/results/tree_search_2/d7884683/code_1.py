def max_partitions():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        dp = {0: 0}
        left_sum = 0
        max_partitions = 0
        
        for i in range(1, n+1):
            left_sum += arr[i-1]
            
            if left_sum not in dp:
                dp[left_sum] = 0
            
            if dp.get(left_sum, 0) > max_partitions:
                max_partitions = dp.get(left_sum, 0)
        
        print(max_partitions)

max_partitions()
