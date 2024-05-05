def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        grid = [input() for _ in range(N)]
        
        count = 0
        dp = [0] * N
        dp[0] = 1 if grid[0][0] == '.' else 0
        
        for i in range(1, N):
            if grid[i][0] == '.':
                dp[i] = dp[i-1]
            else:
                dp[i] = 0
        
        for j in range(1, N):
            if grid[0][j] == '.':
                dp[0] += dp[0]
            else:
                break
        
        for i in range(N):
            count += dp[i]
        
        print(count)

if __name__ == "__main__":
    solve()
