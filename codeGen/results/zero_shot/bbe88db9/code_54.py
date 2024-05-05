# Initialize a variable to store the number of moves
moves = 0

# Start at room 1
room = 1

# While we haven't reached the last room, keep moving
while room != n+1:
    # If we've already painted the ceiling, toggle the direction
    if (room-1) % 2 == 1:
        if graph[room][0] > room:
            room = graph[room][1]
        else:
            room = graph[room][0]
    # If not, just move in one direction
    else:
        room += 1

# Print the number of moves
print(moves)
