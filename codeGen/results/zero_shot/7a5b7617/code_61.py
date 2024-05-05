def count_steady_tables():
    T = int(input())
    MOD = 10**9

    for _ in range(T):
        N, M = map(int, input().split())
        dp = [0] * (M + 1)
        dp[0] = 1
        for i in range(N):
            new_dp = [0] * (M + 1)
            for j in range(M + 1):
                if j <= M:
                    new_dp[j] = (new_dp.get(j, 0) + dp[min(j, M)]) % MOD
            dp = new_dp

        print(sum(dp))  # Print the sum of all row sums modulo MOD

count_steady_tables()
