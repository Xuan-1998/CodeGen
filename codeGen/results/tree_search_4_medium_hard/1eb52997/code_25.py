import sys

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
        
        dp = [[0] * N for _ in range(N)]
        
        def is_safe(i, j):
            # Check if there are no rocks to the East
            for k in range(j + 1, N):
                if grid[i][k] == '#':
                    return False
            return True
        
        def count_mirrors(i, j):
            if dp[i][j]:
                return dp[i][j]
            
            if is_safe(i, j):
                # Place a mirror and recursively count the mirrors to the East
                dp[i][j] = 1 + sum(count_mirrors(k, N - 1) for k in range(N) if k > i)
            else:
                dp[i][j] = 0
            
            return dp[i][j]
        
        total_mirrors = 0
        for i in range(N):
            for j in range(N):
                total_mirrors += count_mirrors(i, j)
                
        print(total_mirrors)

solve()
