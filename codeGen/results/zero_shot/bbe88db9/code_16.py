def solve(n, portals):
    # Initialize the visited array with all False
    visited = [False] * (n + 1)
    
    # Initialize the count of moves
    move_count = 0
    
    # Start from room 1
    current_room = 1
    
    while not visited[n]:
        if current_room == n:
            break
        
        # Check which portal to take based on the number of crosses painted
        if len([i for i in range(current_room) if visited[i]]) % 2 != 0:
            next_room = portals[current_room - 1]
        else:
            next_room = current_room + 1
        
        # Move to the next room and mark it as visited
        current_room = next_room
        visited[current_room - 1] = True
        
        # Increment the move count
        move_count += 1
    
    return move_count % (10**9 + 7)

n = int(input())
portals = list(map(int, input().split()))
print(solve(n, portals))
