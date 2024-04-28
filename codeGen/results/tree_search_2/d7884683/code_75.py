def partition_array():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        # Initialize the dp table and precompute prefix sum
        dp = {}
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + arr[i]
        
        # Fill up the dp table
        max_partitions = 0
        left_sum = 0
        for right_sum in range(prefix_sum[-1]):
            if (i, right_sum) not in dp:
                i += 1
                while i < n and prefix_sum[i] - left_sum == right_sum:
                    i += 1
                if i == n:
                    break
                max_partitions = max(max_partitions, i)
                dp[(i, right_sum)] = i
            
        print(max_partitions)

partition_array()
