# Step 1: Read the input
n = int(input())
p = list(map(int, input().split()))

# Step 2: Create a dictionary to store the portal connections
portals = {i+1: j for i, j in enumerate(p)}

# Step 3: Initialize variables to track the number of crosses and the current room
crosses = [0] * (n+1)
room = 1

# Step 4: Perform a depth-first search to find the shortest path out of the maze
def dfs(room):
    if room == n+1:
        return 0
    
    # If we've already visited this room, return the number of crosses in it
    if crosses[room] > 0:
        return crosses[room]
    
    # Mark the current room as visited
    crosses[room] = (crosses[room-1] + 1) % 2
    
    # Recursively explore the two possible rooms
    left = dfs(portals[room])
    right = dfs(room+1)
    
    # Return the minimum number of moves required to get out from either room
    return min(left, right)

# Step 5: Print the answer
print(dfs(1) % (10**9 + 7))
