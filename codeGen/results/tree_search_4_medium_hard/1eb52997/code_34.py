import sys
from collections import defaultdict

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        grid = [input() for _ in range(N)]
        
        # Initialize memoization dictionary
        memo = defaultdict(int)
        
        def dp(i, j):
            if i == N or j == N:
                return 1
            key = (i, j)
            if memo[key]:
                return memo[key]
            
            if grid[i][j] == '.':
                # If cell is empty, check the cells to the East and recursively call dp
                count = 0
                for k in range(j+1, N):
                    if grid[i][k] == '#':
                        break
                    count += dp(i, k)
                memo[key] = count
                return count
            else:
                # If cell contains a rock, it can't be used as a mirror position
                memo[key] = 0
                return 0
        
        total_count = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j] == '.':
                    total_count += dp(i, j)
        
        print(total_count)

if __name__ == "__main__":
    solve()
