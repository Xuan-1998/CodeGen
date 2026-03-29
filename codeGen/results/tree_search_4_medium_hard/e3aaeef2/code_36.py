def process_input():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        print(solve(n, m))

def solve(n, m):
    mod = 10**9 + 7
    dp = [[0] * (m + 1) for _ in range(11)]

    for i in range(1, 11):
        dp[i][0] = i

    for j in range(1, m + 1):
        for i in range(j + 1):
            if i == 0:
                dp[0][j] = 0
            else:
                dp[i][j] = (dp[(i - 1) // 9 + 1][j - 1] + 1) % mod

    return dp[n % 10][m]

process_input()
