import sys
from collections import defaultdict

def tree_xor(n, k, edges):
    # Step 1: Build the tree structure using adjacency list representation
    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    # Step 2: DFS to find the connected components and their XOR values
    visited = set()
    xor_values = {}
    for node in range(1, n+1):
        if node not in visited:
            component_xor = 0
            stack = [node]
            while stack:
                curr_node = stack.pop()
                if curr_node not in visited:
                    visited.add(curr_node)
                    component_xor ^= a_list[curr_node-1]
                    for neighbor in adj_list[curr_node]:
                        if neighbor not in visited:
                            stack.append(neighbor)
            xor_values[component_xor] = 1

    # Step 3: Check if it's possible to delete at most k-1 edges
    possible = False
    for value, count in xor_values.items():
        if count > 1 or (count == 1 and len(xor_values) <= k):
            possible = True
            break

    return "YES" if possible else "NO"
