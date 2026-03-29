def max_sum_path(tree):
    def max_sum(node, parent=None):
        if node == -1:  # leaf node
            return 0

        left_sum = max_sum(tree[node * 2 + 1], node)
        right_sum = max_sum(tree[node * 2 + 2], node)

        if parent is not None:
            return tree[node] + left_sum + right_sum
        else:
            return max(left_sum, right_sum) + tree[node]

    return max_sum(0)

# Read input from stdin
tree = [int(x) for x in input().split()]

print(max_sum_path(tree))
