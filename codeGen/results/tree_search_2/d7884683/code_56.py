def max_partition():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        dp = {(0, 0): 1}
        total_sum = sum(arr)
        curr_sum = 0
        max_partitions = 0
        
        for i in range(n):
            curr_sum += arr[i]
            if (curr_sum, 0) in dp:
                partitions = dp[(curr_sum, 0)]
            else:
                partitions = 0
            
            if abs(curr_sum - total_sum) <= abs(total_sum // 2 - curr_sum):
                max_partitions = max(max_partitions, partitions + 1)
            
            for j in range(i):
                if (curr_sum - arr[j], j) in dp:
                    partitions = dp[(curr_sum - arr[j], j)]
                else:
                    partitions = 0
                
                if abs(curr_sum - arr[j] - total_sum) <= abs(total_sum // 2 - curr_sum + arr[j]):
                    max_partitions = max(max_partitions, partitions + 1)
            
            dp[(curr_sum, i)] = max(partitions, max_partitions)
        
        print(max_partitions)

max_partition()
