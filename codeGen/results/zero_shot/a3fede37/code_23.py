import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(array, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    node = Node(array[mid])
    node.left = build_tree(array, start, mid - 1)
    node.right = build_tree(array, mid + 1, end)

    return node

def max_path_sum(node):
    if node is None:
        return 0

    left_sum = max_path_sum(node.left)
    right_sum = max_path_sum(node.right)

    current_max_sum = node.value
    if node.left and node.left.value > 0:
        current_max_sum += node.left.value
    if node.right and node.right.value > 0:
        current_max_sum += node.right.value

    return max(left_sum, right_sum, current_max_sum)

input_array = list(map(int, sys.stdin.readline().split()))
root = build_tree(input_array, 0, len(input_array) - 1)
max_sum = max_path_sum(root)
print(max_sum)
