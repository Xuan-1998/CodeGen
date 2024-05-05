import sys

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
        count = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j] == '.':
                    # Check if the cell is visible from the East side
                    if all(grid[i][k] == '.' for k in range(j, N)):
                        count += 1
        print(count)

if __name__ == '__main__':
    solve()
