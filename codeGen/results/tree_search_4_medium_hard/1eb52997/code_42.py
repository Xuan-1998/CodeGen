def count_mirrors(grid):
    T, N = int(input()), int(input())
    mirrors = [0] * N
    
    for i in range(N-1, -1, -1):
        if i == N-1:
            visible_rocks = 0
        else:
            visible_rocks = sum(1 for j in range(i+1, N) if grid[j][i] == '#')
        
        mirrors[i] = sum((grid[j][i] == '.') and (j < i or grid[j][i] == '#') 
                          for j in range(i)) + 1 if visible_rocks == 0 else 0
    
    return sum(mirrors)

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        grid = [list(input()) for _ in range(N)]
        print(count_mirrors(grid))

if __name__ == "__main__":
    main()
