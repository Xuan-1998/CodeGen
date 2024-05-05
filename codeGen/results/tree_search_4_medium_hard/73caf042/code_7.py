def count_diamonds():
    T = int(input())
    for _ in range(T):
        N = int(input())
        dp = [[0] * (N + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                even_sum = sum(int(digit) for digit in str(i + j))
                odd_sum = sum(int(digit) for digit in str(i + j)) - even_sum
                dp[i][j] = dp[i-1][j] if i % 2 == 0 else dp[i][j-1]
                dp[i][j] += abs(even_sum - odd_sum)
        print(dp[-1][-1])

count_diamonds()
