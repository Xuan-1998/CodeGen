def count_stable_tables(N, M):
    # Create a 2D array to store the number of stable tables for each prefix sum
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    # Base case: one row with sum 0 is always possible
    dp[0][0] = 1

    for i in range(1, N + 1):
        for j in range(M + 1):
            if j == 0:
                # The first row can have any sum
                dp[i][j] = dp[i - 1][M]
            else:
                # For each possible sum of the current row,
                # calculate the number of stable tables with that sum
                for k in range(min(j, M)):
                    dp[i][j] += dp[i - 1][k]

    return dp[N][M] % (10**9 + 7)

def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        print(count_stable_tables(N, M))

if __name__ == "__main__":
    main()
