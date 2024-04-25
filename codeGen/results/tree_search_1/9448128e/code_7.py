MOD = 998244353

def solve(N, sets):
    # Initialize the dp array
    dp = [[0, 0] for _ in range(N + 1)]
    dp[0][0] = 1  # Base case: there's one way to form a sequence with 0 sets

    for i in range(1, N + 1):
        sum_dp_prev = sum(dp[i - 1]) % MOD
        # Calculate dp[i][0]
        dp[i][0] = (sum_dp_prev - dp[i - 1][1]) * (len(sets[i - 1]) - 1) % MOD
        # Calculate dp[i][1]
        dp[i][1] = dp[i - 1][0] * max(0, len(sets[i - 1]) - 2) % MOD

    # The answer is the sum of the two possibilities for the last set
    return (dp[N][0] + dp[N][1]) % MOD

def main():
    N = int(input().strip())
    sets = [list(map(int, input().split()))[1:] for _ in range(N)]
    print(solve(N, sets))

if __name__ == "__main__":
    main()
