def expected_non_zero_carries():
    T = int(input())
    for _ in range(T):
        N = int(input())
        dp = [[0] * (N + 1) for _ in range(N + 1)]
        
        # Calculate cumulative sum modulo 10 for each digit position
        cum_sum_A = [0] * (N + 1)
        cum_sum_B = [0] * (N + 1)
        for i in range(1, N + 1):
            cum_sum_A[i] = (cum_sum_A[i - 1] + int(input())) % 10
            cum_sum_B[i] = (cum_sum_B[i - 1] + int(input())) % 10
        
        # Calculate non-zero carries using memoization
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if i == 1:
                    dp[i][j] = (cum_sum_A[j] - cum_sum_B[j]) % 10
                elif j == 1:
                    dp[i][j] = (cum_sum_A[i] - cum_sum_B[i]) % 10
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # Calculate expected number of non-zero carries
        expected_carries = sum([dp[i][j] for i in range(1, N + 1) for j in range(1, N + 1)]) / (N * N)
        print(f"{expected_carries:.6f}")

if __name__ == "__main__":
    expected_non_zero_carries()
