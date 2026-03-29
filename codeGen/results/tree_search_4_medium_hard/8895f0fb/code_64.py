def expected_carries():
    T = int(input())
    for _ in range(T):
        N = int(input())
        dp = [[0.0] * (N + 1) for _ in range(N + 1)]
        carry_prob = 1 / 10.0  # probability of non-zero carry when adding two digits

        for i in range(1, N + 1):
            for j in range(max(0, N - i), min(i, N)):
                dp[i][j] = (dp[max(0, i-1)][max(0, j-1)] + carry_prob * 10 ** (N - i - j))

        answer = sum([sum(row) for row in dp]) / ((N + 1) * (N + 1))
        print(answer)

expected_carries()
