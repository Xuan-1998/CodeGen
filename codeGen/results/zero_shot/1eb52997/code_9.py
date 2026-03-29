def solve():
    T = int(input())
    
    for _ in range(T):
        N = int(input())
        grid = [list(input()) for _ in range(N)]
        
        count = 0
        
        for i in range(N):
            for j in range(N):
                if grid[i][j] == '.':
                    # Check the East side (45 degrees)
                    can_see = True
                    for k in range(j+1, N):
                        if grid[i][k] == '#':
                            can_see = False
                            break
                    
                    if can_see:
                        count += 1
        
        print(count)

solve()
