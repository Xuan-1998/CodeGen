def solve():
    t = int(input())  # Number of test cases
    for _ in range(t):
        n, k, z = map(int, input().split())  # Array size, total moves, and maximum consecutive left moves
        scores = list(map(int, input().split()))  # Array of scores

        dp = [[0] * (k + 1) for _ in range(n + 1)]  # DP table

        for i in range(1, n + 1):
            dp[i][0] = sum(scores[:i])  # Base case: no moves
            for j in range(1, min(i, k) + 1):
                if j <= z:
                    dp[i][j] = max(dp[i - 1][0], dp[i - z][z])
                else:
                    dp[i][j] = dp[i - 1][j - 1] + scores[i - 1]

        print(dp[n][k])  # Print the maximum score

if __name__ == "__main__":
    solve()
