class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def count_trees(p):
    n = int(input())
    p = list(map(int, input().split()))
    root = None
    for i in range(n):
        root = insert(root, p[i])
    return 1 if root is None else 0

print(count_trees(sys.stdin.read().strip().split('\n')[1:]))
