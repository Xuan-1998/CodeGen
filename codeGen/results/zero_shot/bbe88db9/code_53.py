def get_portal_moves(n):
    # Step 1: Initialize the number of portal moves
    portal_moves = 0
    
    # Step 2: Start at room 1 and keep moving until we reach room n+1
    current_room = 1
    while current_room < n + 1:
        # Step 3: Determine which portal to take based on the number of crosses
        if current_room % 2 == 0:  # If the ceiling has an even number of crosses
            next_room = p[current_room - 1]  # Take the first portal (p_i)
        else:  # If the ceiling has an odd number of crosses
            next_room = p[current_room - 1]  # Take the second portal (p_i)
        
        # Step 4: Move to the next room and increment the number of portal moves
        current_room = next_room
        portal_moves += 1
    
    # Step 5: Return the total number of portal moves
    return portal_moves % 1000000007

# Read input from stdin
n = int(input())
p = list(map(int, input().split()))

# Calculate and print the result
print(get_portal_moves(n))
