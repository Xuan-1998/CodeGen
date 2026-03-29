T = int(input())
for _ in range(T):
    N = int(input())
    grid = [input().strip() for _ in range(N)]
    east_sight_count = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '.':
                can_see_east = True
                for k in range(i+1, N):
                    if grid[k][j] == '#':
                        can_see_east = False
                        break
                if can_see_east:
                    east_sight_count += 1
    print(east_sight_count)
