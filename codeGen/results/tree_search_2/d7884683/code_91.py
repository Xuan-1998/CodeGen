def max_partition_size():
    t = int(input())  # number of test cases
    for _ in range(t):
        n = int(input())  # size of the array
        arr = list(map(int, input().split()))  # input array

        dp = {}  # dynamic programming table
        cum_sum = sum(arr)
        for i in range(n-1, -1, -1):
            if i == n-1:
                dp[i] = 0
            else:
                j = i-1
                while j >= 0 and cum_sum - sum(arr[j:]) != sum(arr[:j]):
                    j -= 1
                dp[i] = max(dp.get(j, 0), 1 + (dp.get(i-1, 0) if i > 0 else 0))
            cum_sum -= arr[i]

        print(dp[n-1])  # output the maximum partition size

max_partition_size()
