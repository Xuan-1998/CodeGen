def move(maze, room, crosses):
    if room == maze[0]:
        return crosses
    if crosses % 2 == 1:
        return 1 + move(maze, p_i, crosses + 1)
    else:
        return 1 + move(maze, room - 1, crosses)

n = int(input())
p_i = [int(x) for x in input().split()]
print(move(n + 1, 1, 0) % 1000000007)
