import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    else:
        if val < root.val:
            if root.left is None:
                root.left = Node(val)
            else:
                insert(root.left, val)
        elif val > root.val:
            if root.right is None:
                root.right = Node(val)
            else:
                insert(root.right, val)

def search(root):
    if root is None or root.left is None and root.right is None:
        return None
    else:
        return root.left

n = int(sys.stdin.readline())
recruits = list(map(int, sys.stdin.readline().split()))
officers = Node(0)
untreated_crimes = 0

for recruit in recruits:
    if recruit == -1:  # crime occurred
        officers = search(officers)
        if officers is None:
            untreated_crimes += 1
    else:  # new group of recruits
        for _ in range(recruit):
            insert(officers, _ + 1)

print(untreated_crimes)
