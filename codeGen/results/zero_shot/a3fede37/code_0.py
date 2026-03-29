def max_sum_path(arr, i):
    # Base case: no children
    if 2*i+1 >= len(arr) and 2*i+2 >= len(arr):
        return arr[i]

    # Recursively calculate maximum sum of left and right subtrees
    left_sum = max_sum_path(arr, 2*i+1)
    right_sum = max_sum_path(arr, 2*i+2)

    # Calculate the maximum sum of this path
    curr_sum = arr[i] + max(left_sum, right_sum)

    return curr_sum

def find_max_sum_tree(arr):
    # Find the maximum sum of all paths in the tree
    max_sum = float('-inf')
    for i in range(len(arr)):
        max_sum = max(max_sum, max_sum_path(arr, i))

    return max_sum

# Read input from stdin and print output to stdout
arr = [int(x) for x in input().split()]
print(find_max_sum_tree(arr))
