def compare_trees(t1, t2):
    # Traverse both trees simultaneously using DFS/BFS
    stack = [(t1, t2)]
    while stack:
        node1, node2 = stack.pop()
        if node1.value != node2.value:
            return False  # Nodes don't match
        if node1.left and node2.right:  # Swap children
            stack.append((node1.left, node2.right))
            stack.append((node1.right, node2.left))
        elif node1.left or node2.left:
            stack.append((node1.left, node2.left))  # Left child matches
            if node1.right and node2.right:  # Swap right children
                stack.append((node1.right, node2.right))
            elif node1.right or node2.right:
                stack.append((node1.right, node2.right))  # Right child matches
        return True  # Trees match

# Example usage
s1 = "hello"
s2 = "olleh"

tree1 = string_to_tree(s1)
tree2 = string_to_tree(s2)

result = compare_trees(tree1, tree2)
print(result)  # Should print: True
