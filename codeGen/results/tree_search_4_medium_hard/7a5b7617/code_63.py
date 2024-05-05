def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        sums = [0] * (n + 1)
        
        # base case: when the sum of all rows except the first one are equal to or greater than 1
        for i in range(2, n + 1):
            dp[i][1] = 1
        
        for j in range(2, m + 1):
            dp[0][j] = 1
        
        # fill up the dp table by iterating over each cell from [1][j] to [N][M]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if sums[i - 1] <= j:
                    dp[i][j] = (dp[i - 1][sums[i - 2]] + 1) % 1000000000
                    dp[i][j] += (j - sums[i - 2]) * dp[i - 1][sums[i - 2]]
                else:
                    dp[i][j] = dp[i - 1][j]
                sums[i] = min(sums[i - 1] + j, m)
        
        # print the answer
        print(dp[n][m])

if __name__ == "__main__":
    solve()
