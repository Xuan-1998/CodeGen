import sys

def tree_xor():
    n, k = map(int, input().split())
    node_values = list(map(int, input().split()))
    edges = []
    
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    # Calculate the bitwise XOR of all node values
    total_xor = 0
    for value in node_values:
        total_xor ^= value
    
    # For each edge, check if deleting it would break any connected component
    for u, v in edges:
        # Create a copy of the original node values
        node_values_copy = node_values[:]
        
        # Simulate deleting the edge by merging nodes u and v
        u_val = node_values[u-1]
        v_val = node_values[v-1]
        node_values_copy[u-1] ^= v_val
        
        # Check if all connected components have the same bitwise XOR value
        for i in range(n):
            if node_values_copy[i] ^ total_xor:
                return "NO"
        
    return "YES"

if __name__ == "__main__":
    while True:
        try:
            print(tree_xor())
        except ValueError:
            break
