from collections import defaultdict

def dfs(node, parent, graph, colors, balance_count, total_balanced):
    # Initialize the balance for the current node
    balance = 1 if colors[node] == 'W' else -1
    # Count the current node as a single-node balanced subtree if it's white
    if balance == 0:
        total_balanced[0] += 1
    
    # Traverse the children
    for child in graph[node]:
        if child != parent:
            # Get balance counts from the subtree
            child_balance = dfs(child, node, graph, colors, balance_count, total_balanced)
            # Update the balance for the current node
            balance += child_balance
    
    # If the subtree rooted at this node is balanced, increment the count
    if balance == 0:
        total_balanced[0] += 1
    
    # Update the balance count for the current balance
    balance_count[balance] += 1
    
    return balance

def count_balanced_subtrees(n, parents, colors):
    # Create the graph
    graph = defaultdict(list)
    for i in range(2, n + 1):
        graph[parents[i - 2]].append(i)
        graph[i].append(parents[i - 2])
    
    # Counter for balanced subtrees
    total_balanced = [0]
    # Perform DFS and count balanced subtrees
    balance_count = defaultdict(int)
    dfs(1, 0, graph, colors, balance_count, total_balanced)
    
    return total_balanced[0]

def main():
    # Read the number of test cases
    t = int(input().strip())
    for _ in range(t):
        # Read the number of vertices
        n = int(input().strip())
        # Read the parent information
        parents = list(map(int, input().strip().split()))
        # Read the colors of the vertices
        colors = '0' + input().strip()  # Add a dummy node at the start for 1-based indexing
        # Count and output the number of balanced subtrees
        print(count_balanced_subtrees(n, parents, colors))

if __name__ == "__main__":
    main()
