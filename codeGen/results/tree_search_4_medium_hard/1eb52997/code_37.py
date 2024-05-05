def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        grid = [input() for _ in range(N)]
        
        dp = [[0] * N for _ in range(N)]
        dp[0][0] = 1 if grid[0][0] == '.' else 0
        
        for i in range(1, N):
            for j in range(N):
                if grid[i][j] == '.':
                    if j > 0 and dp[i-1][j-1]:
                        dp[i][j] = 1
                    elif j < N-1 and dp[i-1][j+1]:
                        dp[i][j] = 1
        
        count = sum(row.count(1) for row in dp)
        print(count)

if __name__ == "__main__":
    solve()
