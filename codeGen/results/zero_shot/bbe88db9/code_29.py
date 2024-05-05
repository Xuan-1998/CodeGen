import sys

def main():
    n = int(sys.stdin.readline().strip())
    portals = [int(x) for x in sys.stdin.readline().strip().split()]

    # Initialize the DP array
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Base case: The number of moves to get from room i to itself is 0
    for i in range(n + 1):
        dp[i][i] = 0

    # Fill up the DP array
    for i in range(1, n + 1):
        for j in range(i + 1, n + 2):
            if portals[i - 1] == j:
                dp[i][j] = min(dp[i - 1][i] + 1, dp[i][i] + 1)
            else:
                dp[i][j] = dp[i - 1][j] + 1

    # Print the answer
    print(dp[1][n + 1], end='')

if __name__ == "__main__":
    main()
