import sys

def count_mirrors():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        grid = []
        for _ in range(N):
            line = sys.stdin.readline().strip()
            grid.append(list(line))
        
        mirrors = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j] == '.' and all(grid[k][j] == '.' or k < i for k in range(i)):
                    mirrors += 1
        
        print(mirrors)

count_mirrors()
