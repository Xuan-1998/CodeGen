def max_sum_path(arr, i):
    # Base case: leaf node (no children)
    if 2*i+1 >= len(arr) and 2*i+2 >= len(arr):
        return arr[i]

    # Recursively explore left subtree
    left_sum = float('-inf')
    if 2*i+1 < len(arr):
        left_sum = max_sum_path(arr, 2*i+1)

    # Recursively explore right subtree
    right_sum = float('-inf')
    if 2*i+2 < len(arr):
        right_sum = max_sum_path(arr, 2*i+2)

    # Return the maximum sum of a path starting from node i
    return arr[i] + max(left_sum, right_sum)

def max_sum_binary_tree(arr):
    # Initialize maximum sum to negative infinity
    max_sum = float('-inf')

    # Iterate through all nodes and find the maximum sum
    for i in range(len(arr)):
        max_sum = max(max_sum, max_sum_path(arr, i))

    return max_sum

# Read input from stdin
arr = [int(x) for x in input().split()]

# Calculate and print the maximum sum to stdout
print(max_sum_binary_tree(arr))
