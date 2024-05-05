def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        grid = [input() for _ in range(N)]
        
        dp = [[0] * N for _ in range(N)]
        
        def count_mirrors(i, j):
            if i < 0 or j < 0 or i >= N or j >= N:
                return 1
            if grid[i][j] == '#':
                return 0
            
            if dp[i][j]:
                return dp[i][j]
            
            count = 1 + count_mirrors(i, j+1)
            for k in range(2):
                i2 = i - k
                j2 = j
                while i2 >= 0 and j2 < N and grid[i2][j2] == '.':
                    i2 -= 1
                    j2 += 1
                if i2 < 0 or j2 >= N:
                    count += 1
            dp[i][j] = count
            return count
        
        total_count = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j] == '.':
                    total_count += count_mirrors(i, j)
        
        print(total_count)

if __name__ == "__main__":
    solve()
