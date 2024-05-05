import sys

def find_steady_tables(N, M):
    # Initialize dp array with zeros
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    # Base case: For each row i and column j, if i == 1 or j == 1, the number of steady tables is 1.
    for i in range(2, N + 1):
        dp[i][0] = 1
    for j in range(1, M + 1):
        dp[0][j] = 1

    # Fill up the dp array using dynamic programming
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 1000000000

    # The number of different steady tables is stored in the bottom-right corner of the dp array.
    return dp[N][M]

def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        print(find_steady_tables(N, M))

if __name__ == "__main__":
    main()
