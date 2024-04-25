MOD = 1000000007

def solve(N, K):
    if N == 1:  # Messi cannot receive the ball on the first pass
        return 0
    dp = [0] * (N + 1)
    dp[0] = 1  # Messi starts with the ball
    dp[1] = 0  # Messi cannot receive the ball on the first pass

    for i in range(2, N + 1):
        dp[i] = (dp[i-1] * (K-2) + dp[i-2] * (K-1)) % MOD

    return dp[N]

# Reading number of test cases
T = int(input().strip())
for _ in range(T):
    N, K = map(int, input().strip().split())
    print(solve(N, K))
