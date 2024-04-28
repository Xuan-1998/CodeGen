def max_partitions():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        dp = [False] * (n + 1)
        seen_sums = set()
        total_sum = sum(arr)
        
        for i in range(1, n + 1):
            left_sum = sum(arr[:i])
            right_sum = total_sum - left_sum
            
            if left_sum in seen_sums:
                dp[i] = True
            else:
                seen_sums.add(left_sum)
                dp[i] = dp[i-1]
        
        max_partitions = 0
        for i in range(1, n + 1):
            if dp[i]:
                max_partitions += 1
        
        print(max_partitions)

max_partitions()
