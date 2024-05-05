def max_path_sum(tree, i):
    if not tree[i]:  # Base case: leaf node or empty array
        return 0

    left_sum = max_path_sum(tree, 2*i+1) if 2*i+1 < len(tree) else 0
    right_sum = max_path_sum(tree, 2*i+2) if 2*i+2 < len(tree) else 0

    # Calculate the maximum path sum including the current node
    # Consider both left and right subtrees
    current_sum = tree[i] + max(left_sum, right_sum)

    memo[(i, current_sum)] = current_sum

    return current_sum

def solve():
    n = int(input())  # Get the number of nodes from stdin
    tree = [int(x) for x in input().split()]  # Read the tree array representation

    memo = {}
    max_path_sum_val = max_path_sum(tree, 0)

    print(max_path_sum_val)  # Print the maximum path sum to stdout
