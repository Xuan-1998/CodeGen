from collections import defaultdict

# Function to perform DFS and detect cycles
def dfs(node, graph, visited, rec_stack):
    visited[node] = True
    rec_stack[node] = True

    # Check all neighbors of the current node
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if dfs(neighbor, graph, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            # A cycle is detected
            return True

    rec_stack[node] = False
    return False

# Function to check if the graph is a DAG and return the minimum number of reads
def min_reads(n, graph):
    visited = [False] * (n + 1)
    rec_stack = [False] * (n + 1)

    # Check for cycles in the graph
    for node in range(1, n + 1):
        if not visited[node]:
            if dfs(node, graph, visited, rec_stack):
                return -1  # A cycle is detected

    # If no cycle is detected, the book can be read in one go
    return 1

# Read input and construct the graph
def main():
    t = int(input())  # Read the number of test cases
    for _ in range(t):
        n = int(input())  # Read the number of chapters
        graph = defaultdict(list)
        for i in range(1, n + 1):
            line = list(map(int, input().split()))
            ki = line[0]
            prerequisites = line[1:]
            for prereq in prerequisites:
                graph[prereq].append(i)  # Add edge from prereq to chapter i

        # Output the minimum number of reads
        print(min_reads(n, graph))

if __name__ == "__main__":
    main()
