def find_max_partitions():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        total_sum = sum(arr)
        
        # Initialize the dp array with (0, 0) as the base case.
        dp = [(0, 0)]
        
        left_sum = 0
        for num in arr:
            left_sum += num
            if left_sum * 2 == total_sum:
                right_sum = total_sum - left_sum
                dp.append((left_sum, right_sum))
        
        max_partitions = 0
        i = 1
        while i < len(dp):
            if dp[i][0] == dp[i-1][1]:
                max_partitions += 1
                i += 1
            else:
                break
        
        print(max_partitions)

find_max_partitions()
