MOD = 998244353

def main():
    N = int(input().strip())
    sets = [list(map(int, input().split()))[1:] for _ in range(N)]

    # Initialize the dp array. Since we only need the previous set, we can use a 2D array with 2 rows.
    dp = [{}, {}]
    for x in sets[0]:
        dp[0][x] = 1  # Base case: There's only one way to end with each element in the first set.

    for i in range(1, N):
        sum_of_prev_dp = sum(dp[(i - 1) % 2].values()) % MOD
        dp[i % 2] = {}
        for x in sets[i]:
            # Calculate the value for dp[i][x] using the formula from the intuition
            dp[i % 2][x] = (sum_of_prev_dp - dp[(i - 1) % 2].get(x, 0)) % MOD

    # The answer is the sum of all possible sequences that can end with any element from the last set
    answer = sum(dp[(N - 1) % 2].values()) % MOD
    print(answer)

if __name__ == "__main__":
    main()
