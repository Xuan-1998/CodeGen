def count_diamonds():
    T = int(input())  # read T from stdin

    for _ in range(T):
        N = int(input())  # read N from stdin
        tabulated_dp = [[0] * (N+1) for _ in range(N+1)]

        for i in range(2, N+1):
            for j in range(2, N+1):
                even_sum = sum(int(digit) for digit in str((i-1)*N+j) if int(digit)%2 == 0)
                odd_sum = sum(int(digit) for digit in str((i-1)*N+j) if int(digit)%2 != 0)
                tabulated_dp[i][j] = abs(even_sum - odd_sum)

        print(tabulated_dp[1][1])  # output the result

count_diamonds()
