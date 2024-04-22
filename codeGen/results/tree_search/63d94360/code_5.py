MOD = 1000000007

def ways_to_pass_ball(N, K):
    DP = [[0] * K for _ in range(N + 1)]
    DP[0][0] = 1  # Initial condition: Messi starts with the ball

    for i in range(1, N + 1):
        sum_prev_passes = sum(DP[i - 1]) % MOD
        for j in range(K):
            if j == 0:
                DP[i][j] = (sum_prev_passes - DP[i - 1][j] + MOD) % MOD
            else:
                DP[i][j] = (sum_prev_passes - DP[i - 1][j]) % MOD

    return DP[N][0]

# Read number of test cases
T = int(input().strip())
for _ in range(T):
    N, K = map(int, input().strip().split())
    print(ways_to_pass_ball(N, K))
