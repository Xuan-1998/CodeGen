def get_portal_moves(n, portals):
    # Initialize the number of crosses and the DFS stack
    crosses = 0
    stack = [(1, 0)]  # (room, crosses)

    while stack:
        room, cross_count = stack.pop()
        if room == n + 1:  # We've reached the final room!
            return crosses % 1000000007

        # Decide which portal to use based on the current number of crosses
        next_room = portals[room - 1] if cross_count % 2 else room // 2 + 1
        new_cross_count = cross_count + (next_room % 2)

        # Add the next room to the stack with its updated cross count
        stack.append((next_room, new_cross_count))

    return -1  # Should not reach this point

# Example usage:
n = int(input())  # Read n from stdin
portals = [int(x) for x in input().split()]  # Read portals from stdin
print(get_portal_moves(n, portals))  # Print the result to stdout
