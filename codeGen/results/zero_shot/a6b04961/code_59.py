python
# Step 1: Read input
n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

# Step 2: Sort edges based on their end points
edges.sort()

# Step 3: Initialize variables to keep track of the current path and its length
path = [1]
path_length = 0

# Step 4: Iterate through the sorted edges
for edge in edges:
    u, v = edge
    
    # Check if adding the edge to the current path will increase the path's length
    if (not path or v not in path) and max(path) + 1 == v:
        path.append(v)
        path_length += 1
    else:
        # The edge cannot be added to the current path, so try to form a new tail
        new_tail = [v]
        for i in range(1, len(path)):
            if (not new_tail or path[i] not in new_tail) and max(new_tail) + 1 == path[i]:
                new_tail.append(path[i])
                new_tail_length = len(new_tail)
            else:
                break
        # Update the maximum beauty
        beauty = min(path_length, new_tail_length) * (len(path) - new_tail_length)
        print(beauty)

# If no edges can be added to form a tail, then the current path is already the longest tail
print(path_length * len(path))
