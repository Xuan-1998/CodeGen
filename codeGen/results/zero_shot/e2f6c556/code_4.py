from collections import deque

def min_reads(n, prerequisites):
    # Create a graph and an array to store in-degrees
    graph = [[] for _ in range(n)]
    in_degree = [0] * n
    distance = [0] * n

    # Build the graph and fill the in-degree array
    for i, prereq in enumerate(prerequisites):
        for p in prereq:
            graph[p - 1].append(i)
            in_degree[i] += 1

    # Queue for nodes with in-degree of 0
    q = deque()
    for i in range(n):
        if in_degree[i] == 0:
            q.append(i)

    # Perform topological sort and calculate distances
    read_count = 0
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            distance[neighbor] = max(distance[neighbor], distance[node] + 1)
            read_count = max(read_count, distance[neighbor])
            if in_degree[neighbor] == 0:
                q.append(neighbor)
    
    # If there are nodes with non-zero in-degree, it means there's a cycle
    if any(in_degree):
        return -1
    return read_count + 1  # Add 1 because we start counting from 0

# Read input and process test cases
def main():
    t = int(input())  # Number of test cases
    for _ in range(t):
        n = int(input())
        prerequisites = [list(map(int, input().split()))[1:] for _ in range(n)]
        print(min_reads(n, prerequisites))

if __name__ == "__main__":
    main()
