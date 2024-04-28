def max_partitions(arr):
    n = len(arr)
    dp = {0: 0}

    for i in range(1, n+1):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i:])
        
        if left_sum == right_sum:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = max(dp.get(i-1, 0), 0)
    
    return dp[n]

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))
