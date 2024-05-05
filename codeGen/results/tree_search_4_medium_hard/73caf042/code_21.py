def count_diamonds():
    T = int(input())
    for _ in range(T):
        N = int(input())
        dp = [[0] * (N+1) for _ in range(N+1)]
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i + j - 1 == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = abs((i+j-1) % 2) - (abs((i+j-1) // 10) - (abs((i+j-1) // 100)))
        print(sum([sum(row) for row in dp]))

count_diamonds()
