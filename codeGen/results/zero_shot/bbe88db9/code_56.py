def count_portal_moves(n, portals):
    # Initialize the number of portal moves
    moves = 0
    
    # Initialize the current room
    current_room = 1
    
    # Loop until we reach the last room
    while current_room < n + 1:
        # If this is not the first room and the ceiling has an odd number of crosses, use the second portal
        if current_room > 1 and (moves % 2) == 1:
            current_room = portals[current_room - 1]
        else:
            # Otherwise, use the first portal
            current_room += 1
        
        # Increment the number of moves
        moves += 1
    
    # Return the total number of moves
    return moves % 1000000007
