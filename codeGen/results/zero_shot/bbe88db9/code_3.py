import sys

def maze_portal_moves():
    n = int(sys.stdin.readline())
    p = [int(x) for x in sys.stdin.readline().split()]
    
    rooms = [(i, i+1, p[i-1]) for i in range(1, n+2)]
    
    moves = 0
    path = []
    
    current_room = 1
    while current_room != n+1:
        if len(path) % 2 == 0:  # even number of crosses on the ceiling
            next_room = rooms[current_room-1][1]
        else:  # odd number of crosses on the ceiling
            next_room = rooms[current_room-1][2]
        
        moves += 1
        path.append(current_room)
        current_room = next_room
    
    print(moves % 1000000007)

maze_portal_moves()
