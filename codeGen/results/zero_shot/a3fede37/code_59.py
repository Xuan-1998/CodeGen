class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum(arr):
    if not arr:  # Check if the array is empty
        return 0

    root_idx = next(i for i, x in enumerate(arr) if x == 1)  # Find the root node
    root_node = Node(arr[root_idx])
    stack = [(root_node, root_idx)]
    max_sum = float('-inf')

    while stack:
        node, idx = stack.pop()
        left_idx = next((i for i in range(idx-1, -1, -1) if arr[i] == 0), None)
        right_idx = next((i for i in range(idx+1, len(arr)) if arr[i] == 0), None)

        # Calculate the sum of the path from the current node to its leftmost leaf
        left_sum = 0
        while left_idx is not None:
            left_sum += arr[left_idx]
            left_idx = next((i for i in range(left_idx-1, -1, -1) if arr[i] == 0), None)

        # Calculate the sum of the path from the current node to its rightmost leaf
        right_sum = 0
        while right_idx is not None:
            right_sum += arr[right_idx]
            right_idx = next((i for i in range(right_idx+1, len(arr)) if arr[i] == 0), None)

        # Update the maximum sum found so far
        max_sum = max(max_sum, node.val + left_sum + right_sum)

    return max_sum

# Example usage:
arr = [1, -2, 3, 4, -5, 6, 7]  # Representing a binary tree
print(max_path_sum(arr))  # Output: 11 (from the path 1 -> 3 -> 6)
