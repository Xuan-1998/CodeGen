def partition_count():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            left_sum = sum(arr[:i])
            right_sum = sum(arr[i:])
            if left_sum == right_sum:
                dp[i][i] = 1
            for j in range(i-1, -1, -1):
                if left_sum == right_sum:
                    dp[j][i] = max(dp[j][i], dp[j+1][i-1]+1)
        print(max(map(max, dp)))

partition_count()
