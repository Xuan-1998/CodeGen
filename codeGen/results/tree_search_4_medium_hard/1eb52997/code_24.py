def solution():
    T = int(input())
    for _ in range(T):
        N = int(input())
        grid = [list(input()) for _ in range(N)]
        
        # Initialize dp array with all 1s
        dp = [[1 if cell == '.' else 0 for cell in row] for row in grid]
        
        # Compute the transition relationship using iteration
        for i in range(1, N):
            for j in range(N):
                if grid[i][j] == '.' and all(grid[k][j] == '.' for k in range(i)):
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
        
        # Return the sum of all values in the last row as the total number of possible options
        print(sum(dp[-1]))

if __name__ == "__main__":
    solution()
