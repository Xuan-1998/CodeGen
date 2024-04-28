def max_partition(t):
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        prefix_sum = [0]
        for num in arr:
            prefix_sum.append(prefix_sum[-1] + num)
        
        dp = {0: 0}
        ans = 0
        for i in range(1, n+1):
            for j in range(i):
                if prefix_sum[i] - prefix_sum[j] in dp:
                    dp[prefix_sum[i]] = max(dp.get(prefix_sum[i], 0), dp[prefix_sum[i] - (prefix_sum[i] - prefix_sum[j])] + 1)
            ans = max(ans, dp.get(prefix_sum[i], 0))
        
        print(ans)

max_partition(int(input()))
