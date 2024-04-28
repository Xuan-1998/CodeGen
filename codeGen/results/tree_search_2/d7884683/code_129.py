def max_partitioning():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        dp = [0] * (n + 1)
        total_sum = sum(arr)
        
        # base case: array with only one element
        dp[0] = 0
        
        for i in range(1, n + 1):
            left_sum = sum(arr[:i])
            
            if left_sum == total_sum - left_sum:
                dp[i] = max(dp[i-1], 1)
            else:
                dp[i] = dp[i-1]
        
        print(dp[-1])

max_partitioning()
