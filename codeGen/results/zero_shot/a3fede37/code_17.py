class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def parse_array_into_tree(array):
    if not array:
        return None

    root_value = array[0]
    left_child_values = array[1: (len(array) + 1) // 2]
    right_child_values = array[(len(array) + 1) // 2:]
    root_node = Node(root_value)
    root_node.left = parse_array_into_tree(left_child_values)
    root_node.right = parse_array_into_tree(right_child_values)
    return root_node

def max_path_sum(node):
    if node is None:
        return 0

    # Recursively calculate the maximum sum of a path in the left subtree
    left_sum = max_path_sum(node.left)

    # Recursively calculate the maximum sum of a path in the right subtree
    right_sum = max_path_sum(node.right)

    # Calculate the maximum sum of a path that includes the current node
    current_sum = node.value + (left_sum if left_sum > right_sum else right_sum)

    return max(left_sum, right_sum, current_sum)

def solve():
    array = [int(x) for x in sys.stdin.readline().split()]
    root_node = parse_array_into_tree(array)
    max_sum = max_path_sum(root_node)
    print(max_sum)

if __name__ == "__main__":
    solve()
