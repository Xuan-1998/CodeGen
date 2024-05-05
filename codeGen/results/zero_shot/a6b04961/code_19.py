# Read the input
n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u-1, v-1))

# Sort the edges by their end vertices
edges.sort(key=lambda x: x[1])

# Initialize variables to store the maximum beauty and the tail's ending vertex
max_beauty = 0
tail_ending_vertex = -1

# Iterate over all possible tails
for i in range(n):
    # Initialize a set to store the tail's vertices
    tail_vertices = {i}
    
    # Find the longest simple path that ends at vertex i
    for j in range(i+1, n):
        # Check if there is an edge between vertex j and any vertex in the tail
        has_edge = False
        for k in range(j-1, -1, -1):
            if (k, j) in edges:
                has_edge = True
                break
        
        # If no such edge exists, we can extend the tail with vertex j
        if not has_edge:
            tail_vertices.add(j)
        
        # Update the maximum beauty and the tail's ending vertex if needed
        if len(tail_vertices) > max_beauty // i + 1:
            max_beauty = i * len(tail_vertices)
            tail_ending_vertex = j

# Print the result
print(max_beauty)
