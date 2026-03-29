def expectedCarries():
    T = int(input())
    for _ in range(T):
        N = int(input())
        dp = [0] * (N + 1)
        dp[0] = 0
        for i in range(1, N + 1):
            total_sum = 0
            for k in range(10):
                if k > 4:
                    total_sum += (k - 5) / 9
                else:
                    total_sum += (5 - k) / 9
            dp[i] = total_sum * i + dp[N - i]
        print(sum([i / (N * (N - 1)) for i in dp]) / T)

expectedCarries()
