class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def reconstruct_tree(arr):
    if not arr:
        return None

    root_value = arr[0]
    if len(arr) == 1:
        return Node(root_value)

    left_child_index = 2 * (arr.index(root_value) + 1)
    right_child_index = left_child_index + 1

    root = Node(root_value)
    root.left = reconstruct_tree(arr[left_child_index:])
    root.right = reconstruct_tree(arr[right_child_index:])

    return root

def max_path_sum(node):
    if node is None:
        return 0

    left_sum = max(0, max_path_sum(node.left))
    right_sum = max(0, max_path_sum(node.right))

    return node.value + max(left_sum, right_sum)

def solve():
    arr = [int(x) for x in input().split()]
    root = reconstruct_tree(arr)
    print(max_path_sum(root))

if __name__ == "__main__":
    solve()
