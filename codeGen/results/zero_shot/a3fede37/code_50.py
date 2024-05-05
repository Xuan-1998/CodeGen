class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(arr):
    if not arr:
        return None
    
    root_value = arr[0]
    left_subtree = build_tree(arr[1: (len(arr)+1)//2])
    right_subtree = build_tree(arr[(len(arr)+1)//2:])
    
    return Node(root_value), left_subtree, right_subtree

def max_path_sum(node):
    if not node:
        return 0
    
    left_sum = max_path_sum(node.left)
    right_sum = max_path_sum(node.right)
    
    if node.value + min(left_sum, right_sum) > node.value:
        return node.value + min(left_sum, right_sum)
    else:
        return node.value

def solve():
    arr = list(map(int, input().split()))
    root, left_subtree, right_subtree = build_tree(arr)
    
    max_sum = max_path_sum(root)
    
    print(max_sum)

if __name__ == "__main__":
    solve()
