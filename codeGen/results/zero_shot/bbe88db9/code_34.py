def get_maze_moves(n, portals):
    moves = 0
    # Initialize a dictionary to store the rooms we've visited and their corresponding move counts
    visited_rooms = {1: 0}
    
    current_room = 1
    while current_room != n + 1:
        if current_room in visited_rooms:
            # If we've visited this room before, it means we're moving back through the maze
            moves += 1
        else:
            # Move to the next room based on the portal rules
            if (moves + visited_rooms[current_room - 1]) % 2 == 0:
                current_room = portals[current_room - 1]
            else:
                current_room += 1
        
        # Mark the current room as visited and update its move count
        visited_rooms[current_room] = moves + 1
    
    return (moves + visited_rooms[n]) % (10**9 + 7)

n = int(input())
portals = list(map(int, input().split()))
print(get_maze_moves(n, portals))
