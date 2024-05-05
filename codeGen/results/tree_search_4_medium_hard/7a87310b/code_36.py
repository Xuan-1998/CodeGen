def count_positive_invertible_matrices():
    T = int(input())
    for _ in range(T):
        N = int(input())
        dp = [0] * (N + 1)
        distinct_matrices = [1] + [0] * N
        for i in range(N, -1, -1):
            if i <= 2:
                dp[i] = 0
            else:
                for j in range(i // 2 + 1):
                    k = i - j
                    if j >= 3 and k >= 3:
                        dp[i] += distinct_matrices[j] * distinct_matrices[k]
        print(dp[N])

count_positive_invertible_matrices()
