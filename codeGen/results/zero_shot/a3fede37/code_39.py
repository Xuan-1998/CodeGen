def max_path_sum(root):
    if root < 0:
        return 0

    # Calculate the maximum sum of a path that starts at the current node
    left_max = max(0, max_path_sum(2*root + 1))
    right_max = max(0, max_path_sum(2*root + 2))

    # Return the maximum sum of a path that starts at the current node
    return root + max(left_max, right_max)

# Read the binary tree array from standard input
n = int(input())
tree = [int(x) for x in input().split()]

# Calculate and print the maximum sum of a path
root_index = 0
max_sum = max_path_sum(root_index)
print(max_sum)
