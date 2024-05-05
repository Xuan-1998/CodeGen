def count_matrices():
    T = int(input())
    dp = {0: 1}
    
    for _ in range(T):
        N = int(input())
        if N not in dp:
            for i in range(N, -1, -1):
                if i not in dp:
                    dp[i] = dp.get(i-2, 0) + dp.get(i-1, 0)
        print(dp[N])

count_matrices()
