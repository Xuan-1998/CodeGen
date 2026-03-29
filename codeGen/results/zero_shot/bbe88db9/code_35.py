def get_out_of_maze(n, room):
    if room == n+1:  # reached the last room
        return 0

    crosses = sum(1 for _ in range(room-1)) % 2  # calculate the number of crosses
    if crosses % 2 == 0:
        next_room = p_[room-1]  # use the first portal
    else:
        next_room = room + (p_[room-1] - room) % (n+1)  # use the second portal

    return 1 + get_out_of_maze(n, next_room)

n = int(input())
p_ = [int(x) for x in input().split()]
print(get_out_of_maze(n, 1) % 1000000007)
