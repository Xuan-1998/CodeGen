def max_partitions(arr):
    n = len(arr)
    prefix_sum = [0]
    for num in arr:
        prefix_sum.append(prefix_sum[-1] + num)

    dp = [[0, 0] for _ in range(n+1)]
    for i in range(2, n+1):
        if prefix_sum[i] == prefix_sum[i//2]:
            dp[i][0], dp[i][1] = min(dp[i-1]), max(dp[i-1])
        else:
            if prefix_sum[i//2] - prefix_sum[i//2-1] < prefix_sum[i//2]:
                left_sum, right_sum = 0, prefix_sum[i//2]
            else:
                left_sum, right_sum = prefix_sum[i//2], 0
            for j in range(i//2+1):
                if prefix_sum[j] - left_sum == right_sum:
                    dp[i][0], dp[i][1] = min(dp[j-1][0]+1, dp[i-1][1]), max(dp[j-1][1]+1, dp[i-1][1])
                    break
            else:
                dp[i][0], dp[i][1] = 0, 0

    return dp[-1][1]

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))
