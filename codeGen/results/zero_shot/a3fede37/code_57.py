def solve(input):
    tree = parse_tree(input)
    return max_sum_path(tree)

input = [1, 2, 3, 4, 5]
print(solve(input))  # Output: ?
