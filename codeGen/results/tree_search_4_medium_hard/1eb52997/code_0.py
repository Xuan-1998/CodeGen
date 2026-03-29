def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        grid = [list(input().strip()) for _ in range(N)]
        dp = [[0] * N for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if grid[i][j] == '.':
                    visible = True
                    for k in range(i+1, N):
                        if grid[k][j] == '#':
                            visible = False
                            break
                    dp[i][j] = 1 if visible else 0

        total = sum(sum(row) for row in dp)
        print(total)

if __name__ == "__main__":
    solve()
