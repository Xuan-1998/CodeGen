def find_trees(relatives):
    # Initialize a set to keep track of visited nodes
    visited = set()
    
    # Initialize a variable to store the number of trees
    num_trees = 0
    
    # Iterate over each relative
    for relative in relatives:
        # If this node has not been visited before, it's the root of a new tree
        if relative not in visited:
            # Start a DFS traversal from this node
            stack = [relative]
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    for neighbor in relatives[node]:
                        if neighbor not in visited:
                            stack.append(neighbor)
            num_trees += 1
    
    return num_trees

def main():
    n = int(input())
    relatives = {}
    for i in range(n):
        relative = int(input())
        if i not in relatives:
            relatives[i] = []
        relatives[i].append(relative)

    print(find_trees(relatives))

if __name__ == "__main__":
    main()
