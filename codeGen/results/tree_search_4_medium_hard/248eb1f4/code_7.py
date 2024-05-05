def solve():
    t = int(input())
    for _ in range(t):
        m, x = map(int, input().split())
        dp = [[0] * (x + 1) for _ in range(x + 1)]
        for i in range(1, x + 1):
            if i % 2 == 1:
                for j in range(i - 1, x, m):
                    dp[i][j] = j % m + 1
            else:
                for j in range(i, 0, -m):
                    dp[i][j] = (x - j) % m + 1
        winners = []
        for i in range(1, x + 1):
            winners.append(dp[x][i])
        print(*winners)

if __name__ == "__main__":
    solve()
