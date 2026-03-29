def min_operations(root):
    # Base case: leaf nodes have no children
    if root.children == []:
        return 0

    # Recursively calculate the minimum number of operations for each child
    min_ops = 0
    for child in root.children:
        min_ops += min_operations(child)

    # Calculate the midpoint of the current range and the difference from the node's value
    mid = (root.l + root.r) // 2
    diff = abs(root.val - mid)

    # If the difference is positive, add an array of integers to the node's value
    if diff > 0:
        min_ops += diff

    return min_ops

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        parents = list(map(int, input().split()))
        ranges = []
        for _ in range(n):
            l, r = map(int, input().split())
            ranges.append((l, r))

        # Build the tree and calculate the minimum number of operations
        root = Node(0)
        for i in range(1, n):
            child = Node(i)
            root.children.append(child)
            child.parent = root

        min_ops = 0
        for node in traverse(root):
            min_ops += min_operations(node)

        print(min_ops)

def traverse(node):
    if not node.children:
        yield node
    else:
        for child in node.children:
            yield from traverse(child)
            yield child

class Node:
    def __init__(self, val):
        self.val = val
        self.l = 0
        self.r = 0
        self.parent = None
        self.children = []

if __name__ == "__main__":
    solve()
