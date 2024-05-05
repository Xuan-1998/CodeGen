python
def solve():
    n, k = map(int, input().split())
    node_values = list(map(int, input().split()))
    
    # Initialize an adjacency list to represent the tree
    adj_list = [[] for _ in range(n)]
    
    # Build the tree from the edges given
    for _ in range(n-1):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # Initialize a dictionary to store the bitwise XOR of node values for each connected component
    xor_values = {}
    
    def dfs(node, parent, current_xor):
        if node not in xor_values:
            xor_values[node] = current_xor
        else:
            if xor_values[node] != current_xor:
                return False
        
        for neighbor in adj_list[node]:
            if neighbor == parent:
                continue
            if not dfs(neighbor, node, (current_xor ^ node_values[neighbor])):
                return False
        
        return True
    
    # Check if it's possible to delete at most k-1 edges to make all connected components have the same bitwise XOR of node values
    for i in range(n):
        if not dfs(i, -1, node_values[i]):
            print("NO")
            return
    print("YES")

if __name__ == "__main__":
    solve()
