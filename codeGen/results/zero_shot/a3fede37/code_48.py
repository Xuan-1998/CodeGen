def max_sum_path(tree):
    return max_sum_path(tree, 0)

# read the input from stdin
n = int(input())
tree = [int(x) for x in input().split()]

print(max_sum_path(tree))
