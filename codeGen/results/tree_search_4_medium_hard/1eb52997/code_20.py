from collections import defaultdict

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        grid = [input() for _ in range(N)]
        
        dp = defaultdict(int)
        count = 0
        
        for j in range(N):
            prev_rocks = 0
            for i in range(N-1, -1, -1):
                if grid[i][j] == '#':
                    prev_rocks += 1
                elif grid[i][j] == '.':
                    dp[prev_rocks] += 1
                    count += 1 if prev_rocks == 0 else 0
        
        print(count)

if __name__ == "__main__":
    solve()
