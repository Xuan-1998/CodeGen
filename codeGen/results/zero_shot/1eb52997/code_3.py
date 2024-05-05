import sys

def count_mirrors(N):
    mirrors = 0
    for i in range(N):
        for j in range(i+1, N):
            if grid[i][j] == '.':
                mirrors += 1
    return mirrors

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    grid = [list(input().strip()) for _ in range(N)]
    print(count_mirrors(N))
